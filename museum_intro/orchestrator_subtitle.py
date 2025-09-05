import json

from subtitle_utils import format_ass_timestamp, format_srt_timestamp, generate_srt_ass_file, burn_in_subtitles
from video_preprocess_utils import extract_audio_from_video


# Constants for video processing
INPUT_JSON = "transcript_subtitle.json"
FINAL_VIDEO = "final_output_video.mp4"
CURRENT_VIDEO = "musuem_video.mp4"
VIDEO_WIDTH = 1280
VIDEO_HEIGHT = 720
FONT_PATH = "NotoSansSC-Regular.ttf"
OUTPUT_AUDIO = "extracted_audio.wav" # New constant for extracted audio file

def main():
    """Main function to load video, generate subtitles, and burn them in."""
    
    # Define subtitle file paths
    srt_output_file = "output.srt"
    ass_output_file = "output.ass"

    # 0. Extract audio from the video
    print(f"Extracting audio from {CURRENT_VIDEO}...")
    if not extract_audio_from_video(CURRENT_VIDEO, OUTPUT_AUDIO):
        print("Audio extraction failed. Exiting.")
        return
    print("Audio extraction complete.")

    # a. Load the INPUT_JSON
    try:
        with open(INPUT_JSON, 'r', encoding='utf-8') as f:
            segments = json.load(f)
    except FileNotFoundError:
        print(f"Error: {INPUT_JSON} not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {INPUT_JSON}.")
        return

    # b. Generate ASS and SRT files
    print("Generating SRT and ASS subtitle files...")
    generate_srt_ass_file(
        segments=segments,
        srt_output_path=srt_output_file,
        ass_output_path=ass_output_file,
        video_width=VIDEO_WIDTH,
        video_height=VIDEO_HEIGHT,
        font_path=FONT_PATH,
        font_color="#FFFF00", # Yellow font
        outline_color="#000000", # Black outline
        opacity=0.9,
        margin_bottom_percent=0.05
    )
    print("Subtitle files generated.")

    # c. Burn in subtitle into FINAL_VIDEO
    print(f"Burning subtitles into {CURRENT_VIDEO} to create {FINAL_VIDEO}...")
    burn_in_subtitles(CURRENT_VIDEO, ass_output_file, FINAL_VIDEO, FONT_PATH)
    print("Video processing complete.")

if __name__ == "__main__":
    main()
