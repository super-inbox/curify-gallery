import json
from pathlib import Path
from moviepy.editor import concatenate_videoclips, VideoFileClip, AudioFileClip
from xtts_utils import synthesize_xtts_audio
from t2v_utils import generate_video_clip
from subtitle_utils import generate_ass

# Paths
INPUT_JSON = "segments.json"
OUTPUT_DIR = Path("generated_segments")
OUTPUT_DIR.mkdir(exist_ok=True)
FINAL_VIDEO = "final_output_video.mp4"

VIDEO_WIDTH = 1280
VIDEO_HEIGHT = 720
FONT_PATH = "NotoSansSC-Regular.ttf"
# Speaker WAVs (must exist)
SPEAKER_MAP = {
    "speak_0": "voices/speak_0.wav",
    "speak_1": "voices/speak_1.wav"
}

def generate_from_json(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        segments = json.load(f)

    segment_paths = []

    for i, seg in enumerate(segments):
        seg_id = seg["segment_id"]
        prompt = seg["description"]
        narration = seg["narration"]
        speaker = seg["speak_id"]
        duration = seg["duration"]

        print(f"\n🎬 Segment {seg_id}: Generating video and audio...")

        # Generate video
        video_path = OUTPUT_DIR / f"segment_{seg_id}.mp4"
        generate_video_clip(prompt, duration, str(video_path))

        # Generate TTS
        audio_path = OUTPUT_DIR / f"segment_{seg_id}.wav"
        synthesize_xtts_audio(
            text=narration,
            speaker_wav=SPEAKER_MAP[speaker],
            output_path=str(audio_path)
        )

        # Overlay subtitle
        ass_path = OUTPUT_DIR / f"segment_{seg_id}.ass"
        generate_ass(text=narration, duration=duration, output_path=ass_path, 
                     video_width=VIDEO_WIDTH, video_height=VIDEO_HEIGHT, font_path=FONT_PATH)

        # Combine video + audio + subtitle (via ffmpeg wrapper)
        final_segment = OUTPUT_DIR / f"final_segment_{seg_id}.mp4"
        mux_segment_with_audio_and_subtitles(
            str(video_path), str(audio_path), str(ass_path), str(final_segment)
        )

        segment_paths.append(str(final_segment))

    return segment_paths

def stitch_segments(segment_paths, output_path):
    clips = [VideoFileClip(p) for p in segment_paths]
    final = concatenate_videoclips(clips)
    final.write_videofile(output_path, codec="libx264", audio_codec="aac")
    print(f"\n✅ Final video saved to {output_path}")

# FFmpeg mux wrapper
def mux_segment_with_audio_and_subtitles(video, audio, srt, output):
    import subprocess
    subprocess.run([
        "ffmpeg", "-y",
        "-i", video,
        "-i", audio,
        "-vf", f"subtitles={srt}",
        "-shortest",
        "-c:v", "libx264",
        "-c:a", "aac",
        output
    ], check=True)


if __name__ == "__main__":
    segment_paths = generate_from_json(INPUT_JSON)
    stitch_segments(segment_paths, FINAL_VIDEO)
