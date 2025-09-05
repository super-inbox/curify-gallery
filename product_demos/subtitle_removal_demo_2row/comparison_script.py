from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip, TextClip, clips_array

# === CONFIGURATION ===
original_path = "original.mp4"
subtitle_removed_path = "subtitle_removed.mp4"
curify_logo_path = "curify_logo.png"
output_path = "demo_subtitle_removal.mp4"

target_width = 720

# === LOAD & RESIZE VIDEOS ===
original = VideoFileClip(original_path).resize(width=target_width)
removed = VideoFileClip(subtitle_removed_path).resize(width=target_width)

# === DURATIONS ===
segment_duration = min(original.duration, removed.duration)

# === OVERLAY TEXT (ImageMagick backend) ===
def overlay_text(clip, text, fontsize=40, color='white', stroke_color='black', stroke_width=2):
    txt = (TextClip(
                text,
                fontsize=fontsize,
                font="Arial-Bold",  # works properly with ImageMagick
                color=color,
                stroke_color=stroke_color,
                stroke_width=stroke_width
            )
           .set_duration(clip.duration)
           .set_position(("left", "top")))
    return CompositeVideoClip([clip, txt])

# === CREATE ROWS WITH TEXT LABELS ===
row1 = overlay_text(original.subclip(0, segment_duration), "Original Video")
row2 = overlay_text(removed.subclip(0, segment_duration), "Subtitle Removed")

# === STACK ROWS VERTICALLY ===
stacked = clips_array([[row1], [row2]])

# === OVERLAY CURIFY LOGO WITH LOW OPACITY ===
logo = (
    ImageClip(curify_logo_path, transparent=True)
    .resize(width=180)
    .set_opacity(0.3)   # watermark effect
    .set_duration(stacked.duration)
    .set_position(("right", "bottom"))
    .margin(right=20, bottom=20, opacity=0)
)

final_video = CompositeVideoClip([stacked, logo])

# === EXPORT ===
final_video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
