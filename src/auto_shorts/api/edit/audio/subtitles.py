"""
TODO: Split each section of the subtitle files (srt) to make sure it fits on a small screen
"""

from ._autosub import generate_subtitles as _generate_subtitles


def transcript(audio_path, subtitle_path):
    _generate_subtitles(audio_path, subtitle_path)