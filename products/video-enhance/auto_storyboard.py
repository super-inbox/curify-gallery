import json
import os
import tempfile
import base64
from moviepy.editor import VideoFileClip
from PIL import Image
from openai import OpenAI

from scenedetect import VideoManager, SceneManager
from scenedetect.detectors import ContentDetector
import cv2

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)


def detect_scenes(video_path, threshold=30.0):
    """Detect more scenes by lowering threshold."""
    video_manager = VideoManager([video_path])
    scene_manager = SceneManager()
    scene_manager.add_detector(ContentDetector(threshold=threshold))

    video_manager.start()
    scene_manager.detect_scenes(frame_source=video_manager)

    scene_list = scene_manager.get_scene_list()

    scenes = []
    for start, end in scene_list:
        scenes.append({
            "start_sec": start.get_seconds(),
            "end_sec": end.get_seconds()
        })

    print(f"Detected {len(scenes)} scenes.")
    return scenes


def extract_scene_frames(video_path, scenes):
    """Extract middle-frame from each detected scene."""
    tmpdir = tempfile.mkdtemp()
    frame_paths = []

    cap = cv2.VideoCapture(video_path)

    for i, scene in enumerate(scenes):
        mid = (scene["start_sec"] + scene["end_sec"]) / 2.0
        cap.set(cv2.CAP_PROP_POS_MSEC, mid * 1000)

        success, frame = cap.read()
        if not success:
            print(f"⚠️ Failed to read frame for scene {i}")
            continue

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)

        frame_path = os.path.join(tmpdir, f"scene_{i}.jpg")
        img.save(frame_path, format="JPEG")

        frame_paths.append(frame_path)

    cap.release()
    return frame_paths


def generate_storyboard(video_path: str, output_json: str):
    print("\n🔍 Detecting scenes...")
    scenes = detect_scenes(video_path, threshold=18.0)  # more sensitive
    frames = extract_scene_frames(video_path, scenes)

    print(f"📸 Extracted {len(frames)} frames.")

    # Build messages with schema
    content_list = [
        {
            "type": "text",
            "text": """
You are given keyframes extracted from a video, along with their true start/end timestamps.

TASK:
Create a storyboard JSON describing each scene with:
- start (float seconds)
- end (float seconds)
- text (what happens in that scene)
- sfx_key (short SFX label, e.g., "impact", "whoosh", "engine")
- text_offset (relative start time for the narration text, 0.0–1.0 normalized)
- text_duration (relative length of narration, 0.1–1.0 normalized)

Guidelines:
- Use the provided start/end timestamps exactly.
- Keep text concise but cinematic.
- Only return a JSON array.
"""
        }
    ]

    # Add scene image + timestamps to model
    for i, frame_path in enumerate(frames):
        scene = scenes[i]

        # text block with timestamps
        content_list.append({
            "type": "text",
            "text": f"Scene {i}: start={scene['start_sec']}, end={scene['end_sec']}"
        })

        # image
        with open(frame_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
            data_url = f"data:image/jpeg;base64,{b64}"
            content_list.append({
                "type": "image_url",
                "image_url": {"url": data_url}
            })

    print("\n💬 Sending to GPT-4o...")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": content_list}],
        max_tokens=3000
    )

    raw = response.choices[0].message.content
    print("\n🔧 MODEL RAW OUTPUT:\n", raw)

    # Clean JSON fences safely
    cleaned = raw.strip()
    for fence in ["```json", "```", "```JSON"]:
        cleaned = cleaned.replace(fence, "")
    cleaned = cleaned.strip()

    data = json.loads(cleaned)

    # Save output
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n🎉 Saved storyboard to {output_json}")


if __name__ == "__main__":
    generate_storyboard("oil_crisis.mp4", "storyboard.json")
