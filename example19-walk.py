#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   learning to search through directories"""

import os

## Define a function that stops searching on first match
def find(name, path):
    result = []  # create a record to hold any "hits"
    
    for root, dirs, files in os.walk(path):   # (r, d, f)
        if name in files:
            result.append(os.path.join(root, name))
    # now that we are done...
    return result  # return the list of "hits" that we had


def main():
    name = input("What am I looking for? ")
    path = input("What is the path in which I should search? ")

    print(find(name, path))


if __name__ == "__main__":
    main()
