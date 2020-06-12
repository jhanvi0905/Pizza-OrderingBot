from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class Pizzaform(FormAction):

    def name(self) -> Text:
        return "pizza_form"

    def required_slots(self, tracker: Tracker) -> List[Text]:

        return ["crust", "pizzat", "toppings", "Qty"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "crust": self.from_entity(entity="crust", intent=["order_pizza", "inform"]),
            "pizzat": self.from_entity(entity="pizzat", intent=["order_pizza", "inform"]),
            "toppings": self.from_entity(entity="toppings", intent=["order_pizza", "inform"]),
            "Qty": self.from_entity(entity="Qty", intent=["order_pizza", "inform"])
        }




    def crust_db(self)-> List[Text]:
        return ["thin", "thick"]

    def pizzat_db(self) -> List[Text]:
        return ["american", "neopolitan", "margharita"]

    def toppings_db(self) -> List[Text]:
        return ["capsicum and extra cheese", "extra cheese", "pepproni and extra cheese", "olives and jalpenos", "onions and capsicum", "cheese and pepproni", "extra cheese and pepproni"]

    def is_int1(self, string: Text) -> bool:
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_crust(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any], ):
        if value.lower() in self.crust_db():
            return {"crust": value}
        else:
            dispatcher.utter_template("utter_wrong_crust", tracker)
            return {"crust": None}

    def validate_pizzat(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any], ):
        if value.lower() in self.pizzat_db():
            return {"pizzat" : value}
        else:
            dispatcher.utter_template("utter_wrong_pizzat", tracker)
            return {"pizzat": None}

    def validate_toppings(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any], ):
        if value.lower() in self.toppings_db():
            return {"toppings": value}
        else:
            dispatcher.utter_template("utter_wrong_toppings", tracker)
            return {"toppings": None}

    def validate_Qty(
                     self,
                     value:Text,
                     dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                     domain: Dict[Text, Any], ) :

        if self.is_int1(value) and int(value) > 0:
            return {"Qty": value}
        else:
            return {"Qty": "1"}
    def submit(self, dispatcher, tracker, domain):  # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]

        
        dispatcher.utter_template("utter_submit", tracker)
        return []

