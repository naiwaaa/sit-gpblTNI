from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_hello_world"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Hello World!")

        return []


class ActionGender(Action):
    def name(self):
        return "action_gender"

    def run(self, dispatcher, tracker, domain):
        messageObtained = tracker.latest_message.text.lower()
        if "male" in messageObtained:
            return [SlotSet("gender", "male")]
        elif "female" in messageObtained:
            return [SlotSet("gender", "female")]
        else:
            return [SlotSet("gender", "others")]
