#!/usr/bin/python3
"""Alta3 Research || By RZFeeser
   Review of monday concepts"""

def learninglists():
    """quick review on how lists work"""

    employees = []   # init an empty list

    employees.append("Alice Anderson")  # .append() method inserts a value into the END of the list (opens a single slot)

    print(employees) # print is a "standard function" - display our list on the screen

    print(type(employees))

    employees.append("Bob Barker")  # first poistion
    employees.append("Chester Copperpot") # second position

    print(employees[1]) # should display "bob barker"  ( lists start at zero! )

    print(dir(employees))

    print(employees.count("Bob Barker")) # should say "1"

    employees.append("Bob Barker")

    print(employees.count("Bob Barker")) # now says "2"

    print(employees.pop(0)) # .pop() method removes the value at the INDEX passed, and returns the value removed from the list

    print(employees)  # ["Bob Barker", "Chester Copperpot", "Bob Barker"]

    print(employees[-1])   # grab the very LAST value from the list


def learningdictionaries():
    """a quick review on how dicts work"""

    atreides = {}   # init a dict

    atreides.update({"symbol": "red hawk"}) # add they "key": "value" pair to the dict atreides

    print(atreides) # display the current dict

    atreides["homeworld"] = "caladan"   # a second technique to add to a dict

    print(atreides)

    print(atreides.get("symbol"))    # .get method will search for the key passed to it. returns NONE if the key is not found (by default)
    print(atreides.get("spice production")) # this will NOT be found, but return NONE. Therefore, nothing will be printed to the screen besides a \n
    print(atreides.get("year", "That information is not available")) # in place of NONE, we can return a custom value if the key search is not found\

    print(atreides["homeworld"])    # this technique will produce an ERROR if the key is not found!

    print( atreides.get("homeworld").capitalize() )

    print(atreides.values()) # this will dump to the screen ALL values in a "list list object"


## call our functions
learninglists()
learningdictionaries()
learningdictionaries() # run our custom function a second time
