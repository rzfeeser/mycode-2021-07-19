#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   learning to search through directories"""

import os
import fnmatch

## Define a function that stops searching on first match
def find(pattern, path):
    result = []  # create a record to hold any "hits"
    
    for root, dirs, files in os.walk(path):   # (r, d, f)
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    
    # now that we are done...
    return result  # return the list of "hits" that we had


def main():
    name = input("What pattern am I looking for? ")
    path = input("What is the path in which I should search? ")

    print(find(name, path))


if __name__ == "__main__":
    main()
