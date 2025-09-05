import os
import json
from pathlib import Path
from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline
import torch
from PIL import Image
from openai import OpenAI

client = OpenAI()

# Global story context
story_context_cn = "《博物馆的全能ACE》是一部拟人化博物馆文物与AI讲解助手互动的短片，讲述太阳人石刻在闭馆后的博物馆中，遇到了新来的AI助手博小翼，两者展开对话，AI展示了自己的多模态讲解能力与文化知识，最终被文物们认可，并一起展开智慧导览服务的故事。该片融合了文物拟人化、夜间博物馆奇妙氛围、科技感界面与中国地方文化元素，风格活泼、具未来感。"

# Cache and log directories
CACHE_DIR = Path("prompt_cache")
CACHE_DIR.mkdir(exist_ok=True)
LOG_PATH = Path("prompt_log.jsonl")

# Pipelines
pipe_txt2img = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16).to("cpu")
pipe_img2img = StableDiffusionImg2ImgPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16).to("cpu")

# Reference image context for characters
REFERENCE_CONTEXT = "参考角色视觉信息：'太阳人石刻' 是带有放射状头饰、佩戴墨镜的新石器时代人物形象，风格庄严中略带潮流感。图像见 assets/sunman.png。'博小翼' 是一个圆头圆眼、漂浮型的可爱AI机器人助手，风格拟人、语气亲切，图像见 assets/boxiaoyi.png。"

# Reference image map
ASSET_IMAGES = {
    "太阳人": "assets/sunman.png",
    "博小翼": "assets/boxiaoyi.png"
}

def generate_keyframe_prompt(segment):
    segment_id = segment.get("segment_id")
    cache_file = CACHE_DIR / f"segment_{segment_id}.json"
    if cache_file.exists():
        with open(cache_file, "r", encoding="utf-8") as f:
            return json.load(f)

    description = segment.get("description", "")
    speaker = segment.get("speaker", "")
    narration = segment.get("narration", "")

    input_prompt = f"你是一个擅长视觉脚本设计的AI，请基于以下故事整体背景与分镜内容，帮我生成一个适合用于Stable Diffusion图像生成的英文提示词（image prompt），用于生成低分辨率草图风格的关键帧。请注意突出主要角色、镜头氛围、光影、构图、动作，避免复杂背景和细节。提示词长度不应超过80词，以防止超出Stable Diffusion的token限制。\n\n【整体故事背景】：\n{story_context_cn}\n\n【当前分镜描述】：\n{description}\n【角色】：{speaker}\n【台词或画外音】：{narration}\n\n{REFERENCE_CONTEXT}\n\n请用英文输出一个简洁但具体的prompt，风格偏草图、线稿、卡通、简洁构图，并指出一个negative prompt。"

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert visual prompt designer for image generation."},
                {"role": "user", "content": input_prompt}
            ],
            temperature=0.7
        )
        output_text = response.choices[0].message.content
        if "Negative prompt:" in output_text:
            prompt, negative = output_text.split("Negative prompt:", 1)
        else:
            prompt, negative = output_text, "blurry, distorted, low quality, text, watermark"

        result = {
            "prompt": prompt.strip(),
            "negative_prompt": negative.strip()
        }
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        with open(LOG_PATH, "a", encoding="utf-8") as logf:
            logf.write(json.dumps({"segment_id": segment_id, **result}, ensure_ascii=False) + "\n")
        return result
    except Exception as e:
        print(f"[Error] GPT-4o prompt generation failed for segment {segment_id}: {e}")
        return {
            "prompt": description,
            "negative_prompt": ""
        }

def generate_all_keyframe_images(script_data, output_dir="keyframes"):
    os.makedirs(output_dir, exist_ok=True)
    keyframe_outputs = []

    for segment in script_data:
        sd_prompts = generate_keyframe_prompt(segment)
        prompt = sd_prompts["prompt"]
        negative_prompt = sd_prompts["negative_prompt"]
        segment_id = segment.get("segment_id")

        description = segment.get("description", "")
        use_reference = any(name in description for name in ASSET_IMAGES)

        if use_reference:
            ref_key = next(k for k in ASSET_IMAGES if k in description)
            init_image = Image.open(ASSET_IMAGES[ref_key]).convert("RGB").resize((512, 512))

        frame_images = []
        for i in range(3):
            if use_reference:
                image = pipe_img2img(prompt=prompt, image=init_image, negative_prompt=negative_prompt, strength=0.6, guidance_scale=7.5).images[0]
            else:
                image = pipe_txt2img(prompt, negative_prompt=negative_prompt, num_inference_steps=20, guidance_scale=7.5, height=256, width=256).images[0]

            image_path = os.path.join(output_dir, f"segment_{segment_id}_v{i+1}.png")
            image.save(image_path)
            frame_images.append(image_path)

        keyframe_outputs.append({
            "segment_id": segment_id,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "frame_images": frame_images
        })

        print(f"✓ Generated 3 images for Segment {segment_id} ({'img2img' if use_reference else 'txt2img'})")

    with open("all_prompts_output.json", "w", encoding="utf-8") as f:
        json.dump(keyframe_outputs, f, ensure_ascii=False, indent=2)

    return keyframe_outputs