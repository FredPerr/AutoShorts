from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

from . import DEFAULT_THEME_FONT


def burn_subtitles(subtitles_path, video_path, output_path, theme:dict=DEFAULT_THEME_FONT, **theme_options):
    theme.update(**theme_options)

    
    subtitles = SubtitlesClip(subtitles_path, lambda text: TextClip(text, **theme))
    video = VideoFileClip(video_path)
    combined = CompositeVideoClip([video, subtitles])
    combined.write_videofile(output_path, fps=video.fps)


