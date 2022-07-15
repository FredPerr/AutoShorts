from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.VideoClip import TextClip


from . import DEFAULT_THEME_FONT


def burn(input_file, output_file, text, position=('center', 'center'), t_start=0, t_end=None, fps=25, theme:dict=DEFAULT_THEME_FONT, **theme_options):
    video = VideoFileClip(input_file)
    theme.update(**theme_options)
    txt_clip = TextClip(text, **theme).set_position(position).set_start(t_start).set_end(t_end)

    result = CompositeVideoClip([video, txt_clip]).set_duration(video.duration)
    result.write_videofile(output_file, fps=fps)