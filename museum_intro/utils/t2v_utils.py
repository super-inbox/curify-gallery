import torch
from diffusers.utils import export_to_video
from diffusers import AutoencoderKLWan, WanPipeline
from diffusers.schedulers.scheduling_unipc_multistep import UniPCMultistepScheduler

import mediapy as media

def generate_video_clip(prompt: str, duration: float, video_path: str,
                        negative_prompt: str = "",
                        model_id: str = "Wan-AI/Wan2.1-T2V-1.3B-Diffusers",
                        height: int = 720,
                        width: int = 1280,
                        fps: int = 16,
                        guidance_scale: float = 5.0,
                        flow_shift: float = 5.0):
    vae = AutoencoderKLWan.from_pretrained(model_id, subfolder="vae", torch_dtype=torch.float32)
    scheduler = UniPCMultistepScheduler(prediction_type='flow_prediction', use_flow_sigmas=True, num_train_timesteps=1000, flow_shift=flow_shift)
    pipe = WanPipeline.from_pretrained(model_id, vae=vae, torch_dtype=torch.bfloat16)
    pipe.scheduler = scheduler
    # It's generally recommended to use 'cuda' if available for performance, otherwise 'cpu'
    pipe.to("cuda" if torch.cuda.is_available() else "cpu")

    # Calculate num_frames based on duration and fps
    num_frames = int(duration * fps)

    # Apply default negative prompt if the provided one is empty
    if not negative_prompt:
        negative_prompt = ("Bright tones, overexposed, static, blurred details, subtitles, style, works, paintings, "
                           "images, static, overall gray, worst quality, low quality, JPEG compression residue, ugly, "
                           "incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, "
                           "misshapen limbs, fused fingers, still picture, messy background, three legs, many people in "
                           "the background, walking backwards")

    print(f"Generating video for prompt: '{prompt}' with duration {duration}s ({num_frames} frames at {fps} fps)...")

    output = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        height=height,
        width=width,
        num_frames=num_frames,
        guidance_scale=guidance_scale,
    ).frames[0] # The output of pipe is a list of tensors, we take the first (and usually only) one

    export_to_video(output, video_path, fps=fps)
    print(f"Video saved to: {video_path}")
    return video_path