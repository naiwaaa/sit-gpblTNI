from .bot import RasaBot


class Processor(object):
    def __init__(self):
        self.rasa = RasaBot()

    def process(self, command):
        answer = self.rasa.handle_command(command)
        return answer
