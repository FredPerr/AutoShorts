import os

from moviepy import config

from auto_shorts.api.edit.video import text
from auto_shorts.api.edit import video


def setup():
    config.IMAGEMAGICK_BINARY= r"C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe"


def main():
    setup()
    text.burn('subway30-50.mp4', 'subway30-50text2.mp4', 'Did you kwow', t_start=3, t_end=7)
    # text_to_speech.record_text_to_speech('./', 'hello', 'dd you know that Japan was the largest fish producer since the 1900', lang='fr')
    
