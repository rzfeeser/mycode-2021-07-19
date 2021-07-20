#!/usr/bin/python3
"""Learning about for loops"""


# a list of four items
mylist = ["one", 2, "C", "delta"]


# for loop (counting loop)
for x in mylist:
    print(x) # each time through the loop, x takes on a new value


webster = {"animal": "dog", "insect": "mantis", "fish": "trout"}

print()

for x in webster:
    print(x)   # each time through the loop, this will print the KEY

print()

for x in webster.values():
    print(x)    # each time through the loop, this will print the VALUES

print()


astros = {"people": [{"name": "Mark Vande Hei", "craft": "ISS"}, {"name": "Oleg Novitskiy", "craft": "ISS"}, {"name": "Pyotr Dubrov", "craft": "ISS"}, {"name": "Thomas Pesquet", "craft": "ISS"}, {"name": "Megan McArthur", "craft": "ISS"}, {"name": "Shane Kimbrough", "craft": "ISS"}, {"name": "Akihiko Hoshide", "craft": "ISS"}, {"name": "Nie Haisheng", "craft": "Tiangong"}, {"name": "Liu Boming", "craft": "Tiangong"}, {"name": "Tang Hongbo", "craft": "Tiangong"}], "number": 10, "message": "success"}



for x in astros.get("people"):
    print(x.get("name")) # just display the value of "name", NOT the entire dict
