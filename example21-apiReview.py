#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Ipsum, now with bacon!"""

URL = "https://baconipsum.com/api/?type=meat-and-filler"


# python3 -m pip install requests
import requests

def main():
    """Learning to make API requests"""

    # send HTTP GET to our API target
    resp = requests.get(URL)

    respJson = resp.json()   # strip off JSON that should be attached to a 200 response code

    print(respJson)


# best practice way to call our script
if __name__ == "__main__":
    main()
