#!/usr/bin/python3

# Everything in python is an object
# -Variables, functions and even code

# Every object has an ID, Type and Value
# - ID uniquely identifies a particular instance of an object
#  - Cannot change for the life of the object
# - Type identifies the class of an object
#  - Cannot change for the life of the object
# - Value is the contents of the object
#  - Mutable objects can change value, immutable objects cannot

# All variables in Python are first class objects
# - What looks like a simple variable may be something more complex
# v = some_object()
# print(v)
# c.attrib = 'string'
# v.attribute or v.methods

# Objects in python may be mutable or immutable
# Mutable objects can change value, immutable objects may not
# Distinction is visible using id()
# It appears to change the value

# Most fundamental types in python are immutable
# Numbers, Strings, and tuples are the fundamental types that are immutable
# Integers are immutable objects in Python

# Mutable objects include lists, dictionaries, and some other objects 
# ,depending upon their implementation

def main():
    print("Main starts")
    x = 42
    print("x: Value: %d id: %d" %(x, id(x)))
    print(type(x))
    
    # Now change the value of x
    # This does not actually change the value of x
    # but in reality the variable x now refers to a different integer
    x = 43
    print("x: Value: %d id: %d" %(x, id(x)))
    print(type(x))
    
    # Now again change the value of x to 42
    x = 42
    print("x: Value: %d id: %d" %(x, id(x)))
    print(type(x))
    
    
if __name__ == "__main__": main()
