"""
Download videos from URLs on YouTube.

Possible Features:
    Search for videos with this utility and download them.
"""
from pytube import YouTube, Stream, StreamQuery



def fetch(url, on_progress=None, on_complete=None, **filter_options)-> StreamQuery:
    """
    Fetch the different DASH Stream of the YouTube media.

    Filtering is done using the filter option of the StreamQuery object.
    Use "file_extension='mp4'" to fetch only video streams and "only_audio=True" to fetch only audio streams.

    TODO: Filter for best quality stream (audio & video)
    """
    yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=on_complete)
    return yt.streams.filter(**filter_options)



def download(stream)-> Stream:
    pass