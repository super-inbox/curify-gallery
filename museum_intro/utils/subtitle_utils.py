import logging
import os
from PIL import Image, ImageDraw, ImageFont # Import PIL modules
from datetime import timedelta 
import subprocess

import shlex

logger = logging.getLogger(__name__)

def format_ass_timestamp(seconds: float) -> str:
    """Formats a float timestamp (in seconds) to ASS time format (H:MM:SS.cc)."""
    total_milliseconds = int(seconds * 1000)
    hours = total_milliseconds // 3_600_000
    total_milliseconds %= 3_600_000
    minutes = total_milliseconds // 60_000
    total_milliseconds %= 60_000
    seconds = total_milliseconds // 1_000
    centiseconds = (total_milliseconds % 1_000) // 10
    return f"{hours}:{minutes:02}:{seconds:02}.{centiseconds:02}"

def format_srt_timestamp(seconds: float) -> str:
    """Formats a float timestamp (in seconds) to SRT time format (HH:MM:SS,ms)."""
    td = timedelta(seconds=seconds)
    hours, remainder = divmod(td.total_seconds(), 3600)
    minutes, remainder = divmod(remainder, 60)
    seconds, milliseconds = divmod(remainder, 1)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{int(milliseconds*1000):03}"


def generate_srt_ass_file(
    segments: list,
    srt_output_path: str, # Explicit SRT output path
    ass_output_path: str, # Explicit ASS output path
    video_width: int,
    video_height: int,
    font_path: str,
    font_color: str = "#FFFF00",
    font_name: str = "Noto Sans SC",
    outline_color: str = "#000000",
    opacity: float = 0.9,
    margin_bottom_percent: float = 0.05
) -> None:
    """
    Generates both ASS and SRT subtitle files from a list of segment dictionaries,
    applying styling and positioning logic for ASS.
    """
    # --- ASS Specific Styling Calculations ---
    def hex_to_ass_bgr(hex_color):
        hex_color = hex_color.lstrip('#')
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        return f"&H{b:02X}{g:02X}{r:02X}&"

    ass_font_color = hex_to_ass_bgr(font_color)
    ass_outline_color = hex_to_ass_bgr(outline_color)
    ass_opacity = int((1.0 - opacity) * 255)

    base_font_size = video_height // 22
    if (video_width / video_height) > 16/9:
        subtitle_font_size = int(base_font_size * 0.8)
    elif (video_width / video_height) < 9/16:
        subtitle_font_size = int(base_font_size * 1.2)
    else:
        subtitle_font_size = int(base_font_size)

    dummy_img = Image.new("RGBA", (video_width, 1), (0, 0, 0, 0))
    draw_temp = ImageDraw.Draw(dummy_img)
    try:
        _ = draw_temp.textlength
        text_width_func = lambda txt, fnt: draw_temp.textlength(txt, font=fnt)
    except AttributeError:
        text_width_func = lambda txt, fnt: draw_temp.textsize(txt, font=fnt)[0]

    try:
        font = ImageFont.truetype(font_path, subtitle_font_size)
    except IOError:
        logger.error(f"❌ Font file not found or invalid: {font_path}. Using default font for ASS.")
        font = ImageFont.load_default()
        subtitle_font_size = 24
        outline_width = 1
    else:
        outline_width = max(1, int(subtitle_font_size * 0.05))

    margin_v = int(video_height * margin_bottom_percent)

    try:
        with open(ass_output_path, "w", encoding="utf-8") as ass_f, \
             open(srt_output_path, "w", encoding="utf-8") as srt_f:

            # --- Write ASS Header and Style ---
            ass_f.write("[Script Info]\n")
            ass_f.write("ScriptType: v4.00+\n")
            ass_f.write("PlayResX: {}\n".format(video_width))
            ass_f.write("PlayResY: {}\n".format(video_height))
            ass_f.write("ScaledBorderAndShadow: yes\n")
            ass_f.write("\n")
            ass_f.write("[V4+ Styles]\n")
            ass_f.write(
                f"Style: Default,{font_name},{subtitle_font_size},"
                f"{ass_font_color},{ass_font_color},"
                f"{ass_outline_color},{ass_outline_color},"
                f"0,0,0,0,100,100,0,0,1,{outline_width},0,"
                f"2,{int(video_width*0.05)},{int(video_width*0.05)},{margin_v},1\n"
            )
            ass_f.write("\n")
            ass_f.write("[Events]\n")
            ass_f.write("Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")

            # --- Iterate Segments for both ASS and SRT ---
            for i, segment in enumerate(segments):
                start_time = segment.get("start", 0.0)
                end_time = segment.get("end", 0.0)

                ass_display_text = segment.get("original", "")
                srt_display_text = segment.get("original", "")

                if not ass_display_text and not srt_display_text:
                    continue

                # --- Write to ASS File ---
                subtitle_width_for_wrap = int(video_width * 0.8)
                lines_for_ass = []
                current_line = ""
                words = ass_display_text.replace('\\N', ' ').split()

                for word in words:
                    test_line = f"{current_line} {word}".strip()
                    if current_line == "":
                        test_line = word

                    if text_width_func(test_line, font) <= subtitle_width_for_wrap - (outline_width * 4):
                        current_line = test_line
                    else:
                        lines_for_ass.append(current_line)
                        current_line = word
                lines_for_ass.append(current_line)
                formatted_ass_text = "\\N".join(lines_for_ass)

                ass_f.write(
                    f"Dialogue: 0,"
                    f"{format_ass_timestamp(start_time)},"
                    f"{format_ass_timestamp(end_time)},"
                    f"Default,,"
                    f"0,0,0,,"
                    f"{{\\alpha&H{ass_opacity:02X}&}}{formatted_ass_text}\n"
                )

                # --- Write to SRT File ---
                srt_f.write(f"{i + 1}\n")
                srt_f.write(f"{format_srt_timestamp(start_time)} --> {format_srt_timestamp(end_time)}\n")
                srt_f.write(f"{srt_display_text}\n")
                srt_f.write("\n")

        logger.info(f"ASS file generated successfully at {ass_output_path}")
        logger.info(f"SRT file generated successfully at {srt_output_path}")

    except Exception as e:
        logger.error(f"Error generating subtitle files: {e}", exc_info=True)
        raise

def burn_in_subtitles(video_path: str, subtitle_file_path: str, output_path: str, font_path: str):
    """Burns subtitles into a video using ffmpeg and a custom font."""

    if not os.path.exists(font_path):
        raise FileNotFoundError(f"Font file not found: {font_path}")

    font_dir = os.path.dirname(os.path.abspath(font_path))
    font_name = "Noto Sans SC"

    # Properly escape paths for ffmpeg
    subtitles_arg = f"subtitles={shlex.quote(subtitle_file_path)}:fontsdir={shlex.quote(font_dir)}:force_style='Fontname={font_name}'"

    command = [
        "ffmpeg",
        "-i", video_path,
        "-vf", subtitles_arg,
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "23",
        "-c:a", "copy",
        "-y",
        output_path
    ]

    print("🔧 Executing FFmpeg command:")
    print(" ".join(command))

    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"✅ Subtitles burned into: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ FFmpeg error (code {e.returncode}):\n{e.stderr.decode(errors='ignore')}")
        print("💡 Your FFmpeg build may be missing `libass` support.")
    except FileNotFoundError:
        print("❌ FFmpeg not found. Ensure it’s installed and in PATH.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")