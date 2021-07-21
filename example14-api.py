#!/usr/bin/python3
"""Alta3 Research | By RZFeeser
   API requests with Python -- including best practices"""

import requests

NASAEXAMPLE = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key="   # an API Key is required from api.nasa.gov for this to work!!!

def main():

    with open("../nasa.cred", "r") as nasafile:
        nasakey = nasafile.read().rstrip('\n')   # read our API key out of the open file, and remove any "\n" chars that got picked up (on the right side)

    resp = requests.get(NASAEXAMPLE + nasakey)   # use the requests library to send an HTTP GET to NASAEXAMPLE

    # print(resp.json())                 # .json() strips off a JSON attachment from an HTTP RESPONSE message. print() would then display that data on the screen

    json_from_nasa = resp.json()         # the two steps do the same thing as the single line above
    print(json_from_nasa)

main()
