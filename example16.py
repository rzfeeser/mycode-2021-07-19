#!/usr/bin/python3
"""a script to show how imports work"""

def roger():
    x = "Oh, SideSHOW Bob!"
    return x

def main():
    """runtime code"""
    print("This doesn't need to be complicated to be effective.")
    print(roger())  

# this is how every one of your scripts should be ending!
if __name__ == "__main__":
    main()
