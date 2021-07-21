#!/usr/bin/python3
"""Alta3 Research | By RZFeeser
   API requests with Python -- including best practices"""

import requests

NASAEXAMPLE = "https://api.nasa.gov/neo/rest/v1/feed?" # api description and keys avail from api.nasa.gov

def main():

    # grab our NASA key
    with open("../nasa.cred", "r") as nasafile:
        nasakey = nasafile.read().rstrip('\n')   # read our API key out of the open file, and remove any "\n" chars that got picked up (on the right side)

    # ask for start / end date
    sdate = input("What is the start date of the search (YYYY-MM-DD)? ")
    edate = input("What is the end date of the search (YYYY-MM-DD)? ")


    resp = requests.get(f"{NASAEXAMPLE}start_date={sdate}&end_date={edate}&api_key={nasakey}")   # use the requests library to send an HTTP GET to NASAEXAMPLE 

    if resp.status_code != 200:
        print("Uh oh! You probably typed in invalid dates, or the services is down.")
    else:
        json_from_nasa = resp.json()         # the two steps do the same thing as the single line above
        print(json_from_nasa)

main()
