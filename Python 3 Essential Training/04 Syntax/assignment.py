#!/usr/bin/python3

def main():
    # Assignment operator in python is used a assign value 
    # and create object if not already created
    # Everything in python is a class
    # Create an integer object
    a = 1
    # Create a string object
    b = "two"
    print(a)
    print(type(a))
    print(type(b), b)
    
    # Multiple Assignment can be done in python
    c, d = 3, "four"
    
    print(c, type(c))
    print(d, type(d))
    
    e, f = 5, 6
    print("e = %d, f = %d" %(e, f))
    
    # Swap these values
    e, f = f, e
    print("e = %d, f = %d" %(e, f))
    
    # Sets of values called list, tuples etc.
    # Aggregate types
    # when print is used on an aggregate type 
    # It prints in the same format that is acceptable at the time
    # of object creation
    mytuple = (1, 2, 3, 4, 5)
    print(type(mytuple), mytuple)
    
    mylist = [1, 2, 3, 4, 5]
    print(type(mylist), mylist)
    
    
if __name__ == "__main__":
     main()

# Main allows us to define the function later 
# and can be called before it's definition