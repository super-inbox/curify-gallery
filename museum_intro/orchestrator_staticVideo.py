import json
import os
import re
import base64
import subprocess
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

# Assume _generate_voiceover_coqui_xtts is defined as you provided
# You need `ffmpeg` installed for audio/video processing

# ----------------------------
# Config
# ----------------------------
TARGET_LANGUAGE = "zh"  # or "en"
DESIRED_SPEED = 1.0
SPEAKER_SAMPLE_B64 = "..."  # Base64 of your reference voice sample
OUTPUT_DIR = "museum_v2/output_segments"
FINAL_VIDEO = "museum_v2/final_video.mp4"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def parse_narration(narration_text: str):
    """
    Splits narration into (speaker, text) tuples.
    Handles patterns like:
    太阳人: ...
    博小翼: ...
    """
    lines = narration_text.split("\n")
    parsed = []
    for line in lines:
        # Try to match "Speaker: content"
        match = re.match(r"(.+?):(.*)", line)
        if match:
            speaker = match.group(1).strip()
            content = match.group(2).strip()
            if content:
                parsed.append((speaker, content))
        else:
            # fallback: no speaker label
            parsed.append((None, line.strip()))
    return parsed

def generate_segment_audio(segment_id, narration_text):
    """
    Generate audio file for the segment by concatenating
    all sub-lines of narration.
    """
    parsed_lines = parse_narration(narration_text)
    segment_audio_files = []

    for idx, (speaker, text) in enumerate(parsed_lines):
        audio_path = os.path.join(OUTPUT_DIR, f"segment_{segment_id}_line_{idx}.wav")
        _generate_voiceover_coqui_xtts(
            full_text=text,
            target_language=TARGET_LANGUAGE,
            desired_speed=DESIRED_SPEED,
            output_audio_path=audio_path,
            speaker_sample_b64=SPEAKER_SAMPLE_B64
        )
        segment_audio_files.append(audio_path)

    if len(segment_audio_files) == 1:
        return segment_audio_files[0]

    # Concatenate audio files with ffmpeg
    concat_list_path = os.path.join(OUTPUT_DIR, f"concat_{segment_id}.txt")
    with open(concat_list_path, "w") as f:
        for ap in segment_audio_files:
            f.write(f"file '{os.path.abspath(ap)}'\n")

    merged_audio = os.path.join(OUTPUT_DIR, f"segment_{segment_id}_merged.wav")
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", concat_list_path, "-c", "copy", merged_audio
    ], check=True)

    return merged_audio

def generate_segment_video(segment):
    """
    Generates a video clip from static image and voiceover audio.
    """
    segment_id = segment["segment_id"]
    image_path = f"Final_segment_{segment_id}.png"
    narration = segment.get("narration", "")
    duration = segment.get("duration", 5)

    # Generate audio
    audio_path = generate_segment_audio(segment_id, narration)
    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration  # ensure video matches audio

    # Create static image video with audio
    img_clip = ImageClip(image_path).set_duration(duration).set_audio(audio_clip)
    out_path = os.path.join(OUTPUT_DIR, f"segment_{segment_id}.mp4")
    img_clip.write_videofile(out_path, fps=24, codec="libx264", audio_codec="aac")
    return out_path

def generate_full_video(segments):
    segment_videos = []
    for seg in segments:
        print(f"Processing segment {seg['segment_id']}...")
        seg_video = generate_segment_video(seg)
        segment_videos.append(seg_video)

    # Concatenate segments
    with open(os.path.join(OUTPUT_DIR, "concat_list.txt"), "w") as f:
        for vid in segment_videos:
            f.write(f"file '{os.path.abspath(vid)}'\n")

    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", os.path.join(OUTPUT_DIR, "concat_list.txt"),
        "-c", "copy", FINAL_VIDEO
    ], check=True)
    print(f"✅ Final video saved to {FINAL_VIDEO}")

# ----------------------------
# Usage
# ----------------------------
if __name__ == "__main__":
    with open("segments.json", "r") as f:
        segments = json.load(f)
    generate_full_video(segments)
