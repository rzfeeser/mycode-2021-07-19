#!/usr/bin/python3
"""Alta3 Research | By RZFeeser
   Learning to work with datasets in static files"""

import json

# issfile = open("datasets/issdata.json", "r"
# issfile.read()
# issfile.close() ## no one remembered to do this!!!


with open("datasets/issdata.json", "r") as issfile:
    issdata = issfile.read()  # this will read the entire contents of the file as a STR

print(issdata)   # this should be a block of STR data
print(type(issdata))  # uh oh!! our data is string data :(

# print(issdata.get("people"))  # this WILL NOT WORK! STR objects do not have .get ATTRIBUTES! (methods)

issdict = json.loads(issdata)

# now that it is a dict we can easily pull data from it!
print(issdict)
print(type(issdict))

# just return the LIST mapped to the key "people"
print(issdict.get("people"))

# grab the first entry in the LIST (which is a DICT)
print(issdict.get("people")[0])

# display the value mapped to the key "name"
print(issdict.get("people")[0].get("name"))
