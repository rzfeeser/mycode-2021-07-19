#!/usr/bin/python3
'''Example of using input function
Alta3 Research | By rzfeeser'''


# write the "main" function into memory
def main():
    # print function
    # print("What is your quest?")

    # pause and wait for user input
    quest = input("What is your quest? ")    # always collects STR data

    # print back to the screen what saved with "input"
    print(quest)


    # collect string input
    color = input("What is your favorite color? ")

    ## both of these have the same end result...
    ## but are not the same!

    # pass a series of objects to the print function
    print("Your favorite color is", color)  # print both of these objects to the screen
                                            # seperated by a whitespace sep=" "

    # pass a SINGLE object to the print function
    print("Your favorite color is " + color) # concatenate (add) two strings THEN print to std out 


# call our function
main()
