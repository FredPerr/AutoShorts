"""
Download videos from URLs on YouTube.

Possible Features:
    Search for videos with this utility and download them.
"""
from fileinput import filename
from urllib.error import HTTPError
from pytube import YouTube, Stream, StreamQuery



def fetch(url, on_progress=None, on_complete=None, audio_and_video=False, **filter_options)-> StreamQuery:
    """
    Fetch the different DASH Stream of the YouTube media.
    Video media are ordered by resolution.

    Filtering is done using the filter option of the StreamQuery object.
    Use "only_video=True" to fetch only video streams and "only_audio=True" to fetch only audio streams.
    """
    yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=on_complete)
    filter_options.setdefault('progressive', audio_and_video)
    return yt.streams.filter(**filter_options)


def fetch_best(url, on_progress=None, on_complete=None, type='video'):
    if not type == 'video' and not type == 'audio':
        raise ValueError('The value of "type" should be either "video" or "audio"')

    streams = fetch(url, on_progress, on_complete, type=type, audio_and_video=False)
    if type == 'video':
        return streams.order_by('resolution').last()
    if type == 'audio':
        return streams.order_by('abr').last()



def download(stream: Stream, output_folder: str, filename: str, **kwargs):
    """
    raise: HTTPError if the download failed.
    return: Path where the video was saved.
    """
    return stream.download(output_path=output_folder, filename=f"{filename}.{stream.mime_type.split('/')[1]}", **kwargs)
