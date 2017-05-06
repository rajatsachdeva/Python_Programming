#!/usr/bin/python3

# Classes in python
# Classes in python are how you make objects
# They are blueprint for how an object is created

# An object is an instance of a class
# This is a separate thing
# it's separately encapsulated. it has all of its attributes.
# different objects of a class have their own data space, 
# their own code space ad are essentially their own objects

# define a class
class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    # create an Instance/object of Duck class
    donald = Duck()
    print(donald)
    donald.quack()
    donald.walk()

if __name__ == "__main__": main()
