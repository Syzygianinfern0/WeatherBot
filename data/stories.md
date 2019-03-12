## story1
* greet
   - utter_greet
* ask_weather
   - utter_ask_location
* ask_weather{"city":"London"}
   - slot{"city": "London"}
   - action_get_weather
* goodbye
   - utter_goodbye
## story_002
* greet
   - utter_greet
* ask_weather{"city":"Paris"}
   - slot{"city": "Paris"}
   - action_get_weather
* goodbye
   - utter_goodbye 
## story_003
* greet
   - utter_greet
* ask_weather
   - utter_ask_location
* ask_weather{"city":"Vilnius"}
   - slot{"city": "Vilnius"}
   - action_get_weather
* goodbye
   - utter_goodbye
## story_004
* greet
   - utter_greet
* ask_weather{"location":"Italy"}
   - slot{"location": "Italy"}
   - action_get_weather
* goodbye
   - utter_goodbye 
   
## Generated Story -1714016118649290345
* ask_weather{"city": "Anterdam"}
    - slot{"city": "Anterdam"}
    - action_get_weather
* goodbye
    - utter_goodbye

