import os
import asyncio
import warnings

from rasa.core.agent import Agent

warnings.filterwarnings("ignore")
MODEL_DIR = os.path.dirname(os.path.abspath(__file__))


class RasaBot(object):
    def __init__(self):
        self.agent = Agent.load(f"{MODEL_DIR}/models/current")

    def handle_command(self, command):
        loop = asyncio.get_event_loop()
        answers = loop.run_until_complete(self.agent.handle_message(command))
        answer = " ".join([a["text"] for a in answers])
        return answer
