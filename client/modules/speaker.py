import os

from gtts import gTTS


class Speaker(object):
    def __init__(self):
        pass

    def speak(self, answer):
        print("Generating...")
        tts = gTTS(text=answer, lang="en")
        tts.save("answer.mp3")

        print("Speaking...")
        os.system("mpg321 -q answer.mp3")
        print(f"I said: \t{answer}")
