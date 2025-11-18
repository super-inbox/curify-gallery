import json
import moviepy.editor as mpe
from moviepy.audio.io.AudioFileClip import AudioFileClip
import numpy as np
import os
import math


def load_beats(path):
    with open(path, "r") as f:
        data = json.load(f)

    if isinstance(data, dict) and "beats" in data:
        return data["beats"]
    if isinstance(data, list):
        return data

    raise ValueError("Invalid storyboard format: expected dict['beats'] or list")


# Add background files here later
SFX_LIBRARY = {
    "cash": "sfx/cash.mp3",
    "whoosh": "sfx/whoosh.mp3",
    "dun": "sfx/dun.mp3",
    "clown": "sfx/clown.mp3",
    "news": "sfx/news.mp3",

    # Background SFX (you must add these mp3 files)
    "water_flow": "sfx/water_flow.mp3",
    "evil_laugh": "sfx/evil_laugh.mp3"
}


def mp3_to_wav(path):
    """Convert MP3 → WAV (MoviePy handles WAV much better)."""
    if not path.endswith(".mp3"):
        return path

    wav_path = path.replace(".mp3", ".wav")
    if not os.path.exists(wav_path):
        os.system(f"ffmpeg -y -i '{path}' -ac 2 -ar 44100 '{wav_path}'")
    return wav_path


def build_video(input_video: str, beats_json: str, output_video: str):
    # Remove original audio
    video = mpe.VideoFileClip(input_video).without_audio()
    layers = [video]
    audio_layers = []

    beats = load_beats(beats_json)
    W, H = video.w, video.h

    for beat in beats:
        start = beat["start"]
        end = beat["end"]
        text = beat["text"]
        sfx_key = beat.get("sfx_key")
        bg_sfx_key = beat.get("bg_sfx_key")
        bg_start = beat.get("bg_start", start)
        bg_end = beat.get("bg_end", end)

        text_offset = beat.get("text_offset", 0.2)
        duration = beat.get("text_duration", 2.0)

        # ----------- TEXT LAYER (Reduced Size) -----------
        txt = (
            mpe.TextClip(
                text,
                fontsize=35,
                font="Impact",
                color="white",
                stroke_color="black",
                stroke_width=3,
                method="caption",
                size=(int(W * 0.8), None)
            )
            .set_start(start + text_offset)
            .set_duration(duration)
            .set_position(("center", int(H * 0.82)))
            .crossfadein(0.15)
            .crossfadeout(0.25)
        )
        layers.append(txt)

        # ----------- FOREGROUND SFX (cash, dun, etc.) -----------
        if sfx_key and sfx_key in SFX_LIBRARY:
            wav_path = mp3_to_wav(SFX_LIBRARY[sfx_key])
            sfx = AudioFileClip(wav_path).volumex(1.2).set_start(start + text_offset)
            audio_layers.append(sfx)

        # ----------- BACKGROUND SFX (ambient + evil laugh) -----------
        if bg_sfx_key and bg_sfx_key in SFX_LIBRARY:
            wav_path = mp3_to_wav(SFX_LIBRARY[bg_sfx_key])
            bg_clip = AudioFileClip(wav_path)

            target_duration = bg_end - bg_start

            # If ambient is shorter: loop it
            if bg_clip.duration < target_duration:
                loops = math.ceil(target_duration / bg_clip.duration)
                bg_clip = mpe.concatenate_audioclips([bg_clip] * loops)
            
            # Trim to exact scene portion
            bg_clip = bg_clip.subclip(0, target_duration)

            # Fade in/out for smoother ambient
            bg_clip = bg_clip.audio_fadein(0.5).audio_fadeout(0.5)

            bg_clip = bg_clip.volumex(0.5).set_start(bg_start)
            audio_layers.append(bg_clip)

    # ---- COMBINE ----
    final_audio = mpe.CompositeAudioClip(audio_layers) if audio_layers else None
    final_video = mpe.CompositeVideoClip(layers)

    if final_audio:
        final_video = final_video.set_audio(final_audio)

    final_video.write_videofile(
        output_video,
        codec="libx264",
        audio_codec="aac",
        fps=30
    )

if __name__ == "__main__":
    build_video("oil_crisis.mp4", "storyboard.json", "output_final.mp4")
