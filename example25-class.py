#!/usr/bin/python3
"""understanding class"""

# class 
class Cat:  # this is a factory for creating "Cat" objects
    """we want to track cat objects"""

    # method (function defined inside of a class)
    def __init__(self, name, age): # "init" method
        self.n = name # attribute
        self.a = age  # attribute

    # method (defines what is returned when someone says >>> "print(obj)"
    #def __str__(self): # 2-str, to-str, too-string
    #    return self.n

    def age(self, yearsolder): # this allows our objects to be "aged" by values passed in from the user
        self.a = self.a + yearsolder




# function
def main():
    """runtime code"""
    cat1 = Cat("socks", 3)  # this calls the __init__ method
    
    print(cat1) # this will be a place in memory

    cat1.age(1) # invoke the method ".age"
    
    print(dir(cat1))   # __init__, __str__, n, a, age

    print(cat1.a)
    # result be 4

if __name__ == "__main__":
    main()
