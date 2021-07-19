#!/usr/bin/python3
'''combine input and lists'''


mylist = ["apple", "pear"]


print("currently, the list looks like:", mylist)


addme = input("What should we add to the list? ")


# use the L.append() method to add the value of addme to the end of our list
mylist.append(addme)


print("the new value of the list is:", mylist)
