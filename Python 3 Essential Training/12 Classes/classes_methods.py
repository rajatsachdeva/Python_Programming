#!/usr/bin/python3

# Classes in python
# Using Methods

class Duck:   
    # Constructor method
    # Used to initialize some value
    def __init__(self, value):
        print("construct Duck object")
        self.v = value 
    
    # Methods of class Duck
    # self is a reference to object of class
    # so when the method is called with object it's passed as an argument to method
    def quack(self):
        print('Quaaack!', self.v)

    def walk(self):
        print('Walks like a duck.', self.v)

def main():
    # create an Instance/object of Duck class
    donald = Duck(6)
    donald2 = Duck(97)
    print(donald)
    donald.quack()
    donald.walk()
    print(donald2)
    donald2.quack()
    donald2.walk()

if __name__ == "__main__": main()