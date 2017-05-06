#!/bin/python3

# python is fundamentally an object oriented language
# In python 3 everything is an object

# class is a blueprint of an object
# encapsulation of variables and methods
class Egg:
    # define a constructor
    # with special name __init__
    # All methods within classes have first argument as self
    # which is the reference to object itself
    def __init__(self, kind = "fired"):
        self.kind = kind
    
    def whatKind(self):
        return self.kind
    
def main():
    print("Main starts")
    # Creates an Object of Egg class and 
    # Constructor is called whenever an object is created
    # Here kind will be initialized with default value as fried
    fried = Egg()
    print("fried egg has %s"%(fried.whatKind()))
    
    # Create another object
    scrambled = Egg("scrambled")
    print("scrambled egg has %s"%(scrambled.whatKind()))
    
if __name__ == "__main__":
    main()