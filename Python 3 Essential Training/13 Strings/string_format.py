#!/usr/bin/python3

# In python String are python
# String is an object and the variable containing the string is just a reference to a 
# string object

# Format Methods

def main():
    s = 'this is a string'
    print(s)
    print("id = {}".format(id(s)))
    
    a, b = 5, 42
    print(a, b)
    
    print("a is {} and b is {}".format(a, b))
    s = "a is {} and b is {}"
    print(s.format(a,b))
    
    print("id = {}".format(id(s)))
    
    # Python 2 with % operator overloading
    print("a is %d and b is %d" %(a,b))
    
    print("a is {} and b is {}".format(b, a))
    
    # Positional arguments
    print("a is {1} and b is {0}".format(a, b))
    print("a is {0} and b is {1} and a again is {0}".format(a, b))
    
    # Named arguments
    print("this is {bob} and that is {fred}".format( bob = a, fred = b))
    
    d = dict(bob = a , fred = b)
    print("this is {bob} and that is {fred}".format(**d)) # Here ** makes it kwargs/ Keyword arguments
        
if __name__ == "__main__" : main()