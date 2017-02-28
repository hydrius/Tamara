from brain.tts import GoogleTTS
import threading

class Mouth(object):
    def __init__(self):
        self.tts = GoogleTTS()
        print("")

    def say(self, text, language = "en"):
        """ Check if thread is running then call tts """
        self.tts.say(text, language)


