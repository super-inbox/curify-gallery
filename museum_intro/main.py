from dotenv import load_dotenv
load_dotenv() 

import json
import math
from PIL import Image, ImageDraw
import os
import shutil
from utils.keyframe_utils import generate_keyframe_prompt, generate_all_keyframe_images

# Load segments JSON
def load_segments():
    with open("museum/segments_full.json", "r", encoding="utf-8") as f:
        segments = json.load(f)

    # Select 5 recommended keyframes for preview
    segment_ids_to_preview = [1, 2, 5, 14, 24]
    preview_segments = [s for s in segments if s["segment_id"] in segment_ids_to_preview]
    return preview_segments

# Run the wrapper to generate prompts and images
script_json = load_segments()
generated_sd_prompts = generate_all_keyframe_images(script_json)

# Optionally inspect prompts
# print(json.dumps(generated_sd_prompts, indent=2, ensure_ascii=False))
