"""
TODO: Search for all (included downloaded fonts) in the system "fonts folder".
TODO (in modules): Handle errors to prevent program from crashing or document possible error raised.
"""

from moviepy.video.VideoClip import TextClip


DEFAULT_THEME_FONT = {
    "font": 'Courier',
    "color": 'black',
    "bg_color": 'transparent',
    "font_size": 32,
    "stroke_width": 1,
    "stroke_color": None,
    'method': 'label',
    'align': 'center',
}


def get_colors():
    return TextClip.list('color')


def get_fonts(font_name=None):
    fonts = TextClip.list('font')
    if font_name is None:

        return fonts

    filtered = []
    for font in fonts:
        if font_name in font:
            filtered.append(font)
    return filtered
