#!/usr/bin/python3
"""Alta3 Research | Author: RZFeeser
   A script to review and schedule within cron"""

# import time library
import time

# import requests library
import requests

# define API
API = "https://api.spacexdata.com/v3/dragons/dragon1"


def spacex(ctime):
    """Make call to spacex and write data into a file"""

    # make an API call to spacex (requests)
    resp = requests.get(API)

    # create a file with current timestamp (time)
    with open(f"output/{ctime}-spacex.data", "w") as sxf:
        # write spacex data into file
        sxf.write(resp.text)

    return None # our function finished running


def main():
    """runtime code"""

    # get the current time
    ctime = time.ctime()

    # call custom function spacex
    spacex(ctime)

if __name__ == "__main__":
    main()
