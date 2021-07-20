#!/usr/bin/python3
"""Alta3 Research | By RZFeeser
   Making choices with "if" logic"""


def starship():
    """prompts for entry, and adds to list if entry is valid"""

    # starship registry list
    sshipreg = ["ncc-1701"]

    # prompt user for the "new starship" to be added to sshipreg
    newsship = input("What is the starship you would like to register? ")

    # force collected input data to be lower-case
    newsship = newsship.lower()

    # tests for "true" or "false" - no input is evalualted as "false"
    if (newsship) and (newsship not in sshipreg):
        sshipreg.append(newsship) # given the user didn't just press "enter", add the data to the list
    else: # in all other cases...
        print("That name already appears within the starship regsitry.")

    print(sshipreg)




starship()
