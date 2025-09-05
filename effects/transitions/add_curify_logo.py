from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

def add_logo_to_video(video_path: str, output_path: str, logo_path: str = "curify_log.png"):
    # Load the main video
    video_with_audio = VideoFileClip(video_path)

    # Prepare the logo
    logo = (
        ImageClip(logo_path)
        .set_duration(video_with_audio.duration)
        .resize(height=min(video_with_audio.h / 10, 50))  # max height 50px or 1/10 of video height
        .margin(right=20, bottom=20, opacity=0)           # add transparent margins
        .set_pos(("right", "bottom"))                     # place at bottom right
        .set_opacity(0.3)                                 # semi-transparent
    )

    # Overlay logo on video
    final = CompositeVideoClip([video_with_audio, logo])

    # Export result
    final.write_videofile(output_path, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    add_logo_to_video(
        video_path="demo_video_generation_input.mp4",
        output_path="demo_video_generation.mp4",
        logo_path="curify_logo.png"
    )
