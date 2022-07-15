from moviepy import config

from auto_shorts.api.edit.audio.text_to_speech import record_text_to_speech
from auto_shorts.api.edit.audio.subtitles import transcript


def setup():
    config.IMAGEMAGICK_BINARY= r"C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe"
    config.FFMPEG_BINARY= r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"


def main():
    setup()
    transcript('hello.mp3', 'transcript.flac')
    # record_text_to_speech('./', 'hello', 'Did you know that Japan was the largest fish producer since the 1900s ?', lang='en')
    
    
