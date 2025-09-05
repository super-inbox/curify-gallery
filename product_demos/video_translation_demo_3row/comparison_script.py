from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip, TextClip, clips_array

# === CONFIGURATION ===
english_path = "training_en.mp4"
chinese_path = "training_zh.mp4"
spanish_path = "training_es.mp4"
curify_logo_path = "curify_logo.png"
output_path = "comparison_staged.mp4"

target_width = 720
logo_size = 100

# Labels (can be emoji or text)
labels = {
    "english": "🇺🇸 English",
    "chinese": "🇨🇳 Chinese",
    "spanish": "🇪🇸 Spanish"
}

# === LOAD & RESIZE VIDEOS ===
english = VideoFileClip(english_path).resize(width=target_width)
chinese = VideoFileClip(chinese_path).resize(width=target_width)
spanish = VideoFileClip(spanish_path).resize(width=target_width)

# === DURATIONS ===
segment_duration = min(english.duration, chinese.duration, spanish.duration)

# === CREATE STILLS ===
def freeze_frame(clip, duration):
    return (
        clip.to_ImageClip(t=0)
        .set_duration(duration)
        .set_fps(clip.fps)
    )

# === OVERLAY TEXT LABEL ===
def overlay_text(clip, text, fontsize=40, color="white", stroke_color="black", stroke_width=2):
    txt = (TextClip(
                text,
                fontsize=fontsize,
                font="Arial-Bold",   # pick a font available to ImageMagick
                color=color,
                stroke_color=stroke_color,
                stroke_width=stroke_width
            )
           .set_duration(clip.duration)
           .set_position(("left", "top")))
    return CompositeVideoClip([clip, txt])

def make_labeled_row(row_clip, text, duration=None):
    if duration:
        row_clip = row_clip.subclip(0, duration)
    return overlay_text(row_clip, text)

# === STAGE 1: English plays ===
row1 = make_labeled_row(english.subclip(0, segment_duration), labels["english"])
row2 = overlay_text(freeze_frame(chinese, segment_duration), labels["chinese"])
row3 = overlay_text(freeze_frame(spanish, segment_duration), labels["spanish"])
stage1 = clips_array([[row1], [row2], [row3]])

# === STAGE 2: Chinese plays ===
row1 = overlay_text(freeze_frame(english, segment_duration), labels["english"])
row2 = make_labeled_row(chinese.subclip(0, segment_duration), labels["chinese"])
row3 = overlay_text(freeze_frame(spanish, segment_duration), labels["spanish"])
stage2 = clips_array([[row1], [row2], [row3]])

# === STAGE 3: Spanish plays ===
row1 = overlay_text(freeze_frame(english, segment_duration), labels["english"])
row2 = overlay_text(freeze_frame(chinese, segment_duration), labels["chinese"])
row3 = make_labeled_row(spanish.subclip(0, segment_duration), labels["spanish"])
stage3 = clips_array([[row1], [row2], [row3]])

# === CONCATENATE STAGES ===
full_video = CompositeVideoClip([
    stage1,
    stage2.set_start(segment_duration),
    stage3.set_start(2 * segment_duration)
])
full_video = full_video.set_duration(3 * segment_duration)

# === OVERLAY CURIFY LOGO (watermark style) ===
logo = (
    ImageClip(curify_logo_path, transparent=True)
    .resize(width=logo_size)
    .set_opacity(0.3)
    .set_duration(full_video.duration)
    .set_position(("right", "bottom"))
    .margin(right=20, bottom=20, opacity=0)
)

final_video = CompositeVideoClip([full_video, logo])

# === EXPORT ===
final_video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
