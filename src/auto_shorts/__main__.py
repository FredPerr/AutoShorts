from auto_shorts.api import download

def main():
    stream = download.fetch_best('https://www.youtube.com/watch?v=WEquv0Lyxow&list=RDWEquv0Lyxow&start_radio=1', type='audio')
    print(stream)
    print(download.download(stream, './', 'test'))

    
