import subprocess


MEDIA_PLAYER_EXE = None


def play(media_path):
    if not MEDIA_PLAYER_EXE:
        raise ValueError("The path of the executable of the media player was never provided.")
    subprocess.run((MEDIA_PLAYER_EXE, media_path))