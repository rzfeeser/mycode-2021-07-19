#!/usr/bin/python3
"""Lab 24 - challenge 01""" 

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


for farm in farms:
    print(farm.get("name"), end=": ")
    
    for animal in farm.get("agriculture"):
        if animal == farm.get("agriculture")[-1]:
            print(animal)
        else:
            print(animal, end=", ")
