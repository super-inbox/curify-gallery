from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

# === CONFIGURATION ===
input_path = "input_politics.mp4"
curify_logo_path = "curify_logo.png"
output_path = "politics_with_logo.mp4"

target_width = 720

# === LOAD & RESIZE VIDEO ===
video = VideoFileClip(input_path).resize(width=target_width)

# === CREATE LOGO CLIP ===
logo = (
    ImageClip(curify_logo_path, transparent=True)
    .resize(width=120)          # resize logo
    .set_opacity(0.4)           # watermark style
    .set_duration(video.duration)
    .set_position(("right", "bottom"))
    .margin(right=20, bottom=20, opacity=0)  # padding from edges
)

# === COMBINE VIDEO + LOGO ===
final_video = CompositeVideoClip([video, logo])

# === EXPORT ===
final_video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
