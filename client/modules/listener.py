import speech_recognition as sr


class Listener(object):
    def __init__(self):
        self.r = sr.Recognizer()

    def listen_from_mic(self, device_index=None):
        with sr.Microphone(device_index=device_index) as source:
            self.r.adjust_for_ambient_noise(source)
            print(self.r.energy_threshold)
            # self.r.dynamic_energy_threshold = False
            try:
                print("Listening...")
                audio = self.r.listen(source, timeout=5, phrase_time_limit=3)
                print("Recognizing...")
                return self._recognize(audio)
            except sr.WaitTimeoutError:
                print("<timeout>")
                return "<timeout>"

    def listen_from_file(self, filepath):
        with sr.AudioFile(filepath) as source:
            audio = self.r.record(source)
            return self._recognize(audio)

    def _recognize(self, audio):
        command = ""
        try:
            command = self.r.recognize_google(audio)
            print(f"You said:\t{command}")
            return command
        except sr.WaitTimeoutError:
            print("<timeout>")
            return "<timeout>"
        except sr.UnknownValueError:
            print("<unknownvalue>")
            return "<unknownvalue>"
        except sr.RequestError as e:
            print(f"{e}")
