from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests, json 

class ActionGetWeather(Action):
    def name(self):
        return "action_get_weather"
    
    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot('city')
        api_key = "374b7fbffe367b0c2974e656fdeab696"
        
        skeleton = "https://api.openweathermap.org/data/2.5/weather?"
        complete_url = skeleton + "q=" + city + "&APPID=" + api_key
        
        response = requests.get(complete_url)

        data = response.json()
        
        x=data['main']
        temp = round(x['temp'] - 273.15, 2)
        place = data["name"]
        x = data['weather']
        desc = x[0]['main']

        weather_data = "It's {}*C currently in {}. The weather can be described as {}".format(temp, place, desc)
        dispatcher.utter_message(weather_data)

        return [SlotSet("city", city)]
