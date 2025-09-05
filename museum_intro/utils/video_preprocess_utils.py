# utils/video_preprocess_utils.py
import logging
import os
from moviepy.editor import VideoFileClip

logger = logging.getLogger(__name__)

def extract_audio_from_video(video_path: str, output_audio_path: str) -> bool:
    """
    Extracts the full audio track from a video file and saves it as a WAV file.
    Returns True if successful, False otherwise.
    """
    video_clip = None
    try:
        logger.info(f"Extracting full audio from video: {video_path} to {output_audio_path}")
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_audio_path, codec='pcm_s16le', logger=None)
        audio_clip.close()
        logger.info(f"Full audio extracted to: {output_audio_path}")
        return True
    except Exception as e:
        logger.error(f"Error extracting audio from video {video_path}: {e}", exc_info=True)
        return False
    finally:
        if video_clip:
            video_clip.close()
