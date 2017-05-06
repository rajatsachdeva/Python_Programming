#!/bin/python3

# Finding the type and identity of a variable
# Everything is object and each object has an ID which is unique

def main():
    print("Main Starts !")
    x = 42
    print("x:",x)
    print("id of  x:",id(x))
    print("id of 42:",id(42))
    print("type of  x:", type(x))
    print("type of 42:", type(42))
    # ID of x and 42 is same as the object x references to 
    # integer 42 and thus have the same ID
    # So, Number 42 is an object
    
    y = 42 
    print("y:",y)
    print("id of  y:",id(y))
    print("id of 42:",id(42))
    print("type of  y:", type(y))
    print("type of 42:", type(42))
    
    # == operator compares the value
    print("x == y:", x == y)
    # They are exactly the same objects
    # As they have the same id
    # 'is' compares the id rather than the value
    print("x is y:", x is y)
    
    z = dict(x = 42)
    print(type(z))
    print(z)
    print(id(z))
    
    z2 = dict(x = 42)
    print(type(z2))
    print(z2)
    print(id(z2))
    
    print("z == z2:", z == z2) # True
    print("z is z2:", z is z2) # False as they are differnt objects 
    
    # All muttable objects gets unique ID
    # Whereas the immutable objects get different ID 
    # Variables in python are references to objects
    
if __name__ == "__main__": main()