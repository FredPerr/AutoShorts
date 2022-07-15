from moviepy.video.io.VideoFileClip import VideoFileClip


def keep(input_file, output_file, from_sec, to_sec, audio=True, **write_options):
    video = VideoFileClip(input_file).subclip(from_sec, to_sec)
    video.write_videofile(output_file, audio=audio, **write_options)
