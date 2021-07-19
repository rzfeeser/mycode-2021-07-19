#!/usr/bin/env python3
"""

How to open a file from an external source
and read in the data... as a string

list:
["this", "is", "not", "equal, "to"]

string:
"['this', 'down', 'here']"

"""


#open file, in "r"ead mode
filelist = open("challenge.txt", "r")

# print the object type produced by filelist.read()
print(filelist.read())   # the .read() method reads string data from the file

# reveal the type
print(type(filelist.read()))
