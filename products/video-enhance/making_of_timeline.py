import json
import moviepy.editor as mpe
from moviepy.video.tools.segmenting import findObjects
from moviepy.video.fx.resize import resize
from PIL import Image, ImageDraw, ImageFont
import textwrap

def load_beats(path):
    with open(path, "r") as f:
        data = json.load(f)

    if isinstance(data, dict) and "beats" in data:
        return data["beats"]
    if isinstance(data, list):
        return data
    raise ValueError("Storyboard JSON must contain a list of scenes.")

def make_storyboard_breakdown(beats, width=1080, height=1920, duration=4):
    frames = []
    w, h = width, height
    
    # --- FONT CONFIGURATION ---
    font_path = "NotoSansSC-Regular.ttf"
    
    try:
        # Massive sizes: Title ~140px, Body ~90px, SFX ~70px
        title_font = ImageFont.truetype(font_path, 90)
        body_font = ImageFont.truetype(font_path, 60)
        sfx_font = ImageFont.truetype(font_path, 50)
    except OSError:
        print(f"❌ ERROR: Could not find '{font_path}'.")
        print("Please verify the file is in this directory.")
        # Fallback to prevent crash, though text will be tiny
        title_font = ImageFont.load_default()
        body_font = ImageFont.load_default()
        sfx_font = ImageFont.load_default()

    def draw_text_block(draw, text, x, y, font, fill, max_width):
        """Helper to wrap text and return new Y position"""
        lines = []
        words = text.split()
        current_line = []
        
        # Calculate wrapping
        for word in words:
            test_line = ' '.join(current_line + [word])
            # getbbox returns (left, top, right, bottom)
            bbox = draw.textbbox((0, 0), test_line, font=font)
            text_width = bbox[2] - bbox[0]
            
            if text_width <= max_width:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
        lines.append(' '.join(current_line))
        
        # Draw lines
        current_y = y
        for line in lines:
            bbox = draw.textbbox((x, current_y), line, font=font)
            line_height = bbox[3] - bbox[1]
            draw.text((x, current_y), line, font=font, fill=fill)
            current_y += line_height + 20 # Add padding between lines
            
        return current_y

    # --- GENERATE FRAMES ---
    for i, current_beat in enumerate(beats):
        # Dark background (Dark Slate Grey)
        img = Image.new("RGB", (w, h), color=(30, 35, 40))
        draw = ImageDraw.Draw(img)

        # Header
        draw.text((50, 60), "STORYBOARD", font=title_font, fill="white")
        draw.line([(50, 230), (w-50, 230)], fill="white", width=5)

        y_cursor = 280
        
        for j, b in enumerate(beats):
            is_active = (i == j)
            
            # Visual Style
            if is_active:
                # Bright Yellow text for active beat
                text_color = "#FFE800" 
                time_color = "#00FFCC" # Cyan
                bar_color = "#FFE800"
                opacity = 255
            else:
                # Dimmed Grey for inactive
                text_color = "#777777"
                time_color = "#777777"
                bar_color = "#444444"
                opacity = 100

            start_y = y_cursor
            
            # 1. Time Range
            time_str = f"[{b['start']:.1f}s - {b['end']:.1f}s]"
            draw.text((90, y_cursor), time_str, font=sfx_font, fill=time_color)
            y_cursor += 90

            # 2. Main Action Text (Wrapped)
            y_cursor = draw_text_block(
                draw, 
                b['text'], 
                90,            # X pos 
                y_cursor,      # Y pos
                body_font, 
                text_color, 
                w - 150        # Max width
            )
            
            # 3. SFX Line
            sfx_val = b.get('sfx_key', '—')
            draw.text((90, y_cursor), f"SFX: {sfx_val}", font=sfx_font, fill=time_color)
            
            # Draw vertical bar indicator on the left
            total_block_height = (y_cursor + 80) - start_y
            draw.rectangle(
                [30, start_y, 60, y_cursor + 70], 
                fill=bar_color
            )

            # Space between beats
            y_cursor += 140

        frame_path = f"/tmp/story_frame_{i}.jpg"
        img.save(frame_path)
        frames.append(frame_path)

    # Create video clip
    clips = [mpe.ImageClip(f).set_duration(duration / len(frames)) for f in frames]
    final_clip = mpe.concatenate_videoclips(clips)
    
    return final_clip

def generate_making_of(
    input_video: str,
    enhanced_video: str,
    storyboard_json: str,
    output_video: str = "making_of.mp4",
):
    # Load storyboard
    beats = load_beats(storyboard_json)

    # Load video clips
    clip_original = mpe.VideoFileClip(input_video)
    clip_enhanced = mpe.VideoFileClip(enhanced_video)

    # Duration to showcase
    showcase_start = beats[0]["start"]
    showcase_end = beats[0]["start"] + 6

    # ---- SEGMENT 1: Final Enhanced Clip ----
    seg1 = (
        clip_enhanced.subclip(showcase_start, showcase_end)
        .resize(height=900)
        .set_position(("center", "center"))
        .margin(top=100, opacity=0)
    )
    seg1_text = mpe.TextClip(
        "🔥 Final Enhanced Version",
        fontsize=70,
        color="white",
        font="Impact",
        stroke_color="black",
        stroke_width=4,
    ).set_duration(4).set_position(("center", 50))

    seg1 = mpe.CompositeVideoClip([seg1, seg1_text], size=(1080, 1920)).set_duration(4)

    # ---- SEGMENT 2: Original Clip ----
    seg2 = (
        clip_original.subclip(showcase_start, showcase_end)
        .resize(height=900)
        .set_position(("center", "center"))
        .margin(top=100, opacity=0)
    )
    seg2_text = mpe.TextClip(
        "🎥 Original Footage",
        fontsize=70,
        color="white",
        font="Impact",
        stroke_color="black",
        stroke_width=4,
    ).set_duration(4).set_position(("center", 50))

    seg2 = mpe.CompositeVideoClip([seg2, seg2_text], size=(1080, 1920)).set_duration(4)

    # ---- SEGMENT 3: Storyboard Breakdown ----
    seg3 = make_storyboard_breakdown(beats, width=1080, height=1920, duration=4)

    # ---- SEGMENT 4: Before vs After Side-by-Side ----
    left = clip_original.subclip(showcase_start, showcase_end).resize(height=900)
    right = clip_enhanced.subclip(showcase_start, showcase_end).resize(height=900)

    pair = mpe.clips_array([[left, right]])
    pair = pair.resize(width=1080).set_position(("center", "center"))
    seg4_text = mpe.TextClip(
        "Before ⟷ After",
        fontsize=70,
        color="white",
        stroke_color="black",
        stroke_width=4,
    ).set_duration(6).set_position(("center", 50))

    seg4 = mpe.CompositeVideoClip([pair, seg4_text], size=(1080, 1920)).set_duration(4)

    # ---- CONCAT ALL ----
    final = mpe.concatenate_videoclips([seg1, seg2, seg3, seg4], method="compose")

    final.write_videofile(
        output_video,
        fps=30,
        codec="libx264",
        audio_codec="aac",
    )

    print(f"🎉 Making-of timeline saved to {output_video}")


if __name__ == "__main__":
    generate_making_of(
        input_video="oil_crisis_original.mp4",
        enhanced_video="oil_crisis_enhanced.mp4",
        storyboard_json="storyboard.json",
        output_video="making_of_timeline.mp4"
    )
