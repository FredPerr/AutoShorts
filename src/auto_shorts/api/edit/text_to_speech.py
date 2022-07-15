from gtts import gTTS

def record_text_to_speech(path, filename, text, lang='en', slow=False):
    tts = gTTS(text, lang=lang)
    tts.save(path + filename + '.mp3')