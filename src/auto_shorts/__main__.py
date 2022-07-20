import os
from pathlib import Path

from moviepy import config
from moviepy.video.tools.subtitles import file_to_subtitles

from auto_shorts.api.edit.audio.text_to_speech import record_text_to_speech
from auto_shorts.api.edit.audio.subtitles import transcript
from auto_shorts.api.edit.video.subtitles import burn_subtitles
from auto_shorts.api.edit.video.cut import keep
from auto_shorts.api.edit.video.text import burn
from auto_shorts.interface import video_player


BASE_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent.parent


def setup():
    config.IMAGEMAGICK_BINARY= r"C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe"
    config.FFMPEG_BINARY= r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"
    video_player.MEDIA_PLAYER_EXE = 'C:/Program Files/VideoLAN/VLC/vlc.exe'


def main():
    setup()
    # keep('subway.mp4', 'subway-cut.mp4', 10, 30)
    burn_subtitles('transcript.srt', 'subway-cut.mp4', 'subway-cut-sub.mp4', )
    video_player.play(BASE_DIR / 'subway-cut-sub.mp4')
    # burn('subway-cut-sub.mp4', 'subway-cut-sub.mp4', 'testing')
    x = file_to_subtitles('transcript.srt')
    # print(x)
    # transcript('hello.mp3', 'transcript.srt')
    # record_text_to_speech('./', 'hello', 'Did you know that Japan was the largest fish producer since the 1900s. This is how the fisherman made money in the first place?', lang='en')    
    
    
