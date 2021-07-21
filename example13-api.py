#!/usr/bin/python3
"""Alta3 Research | By RZFeeser
   API requests with Python"""

import requests

NASAEXAMPLE = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY"

resp = requests.get(NASAEXAMPLE)   # use the requests library to send an HTTP GET to NASAEXAMPLE

# print(resp.json())                 # .json() strips off a JSON attachment from an HTTP RESPONSE message. print() would then display that data on the screen

json_from_nasa = resp.json()         # the two steps do the same thing as the single line above
print(json_from_nasa)
