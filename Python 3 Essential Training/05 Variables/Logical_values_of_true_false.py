#!/bin/python3

def main():
    print("Main Starts")
    a, b = 0 , 1
    
    # Equality Operator that equates b/w values
    # True/False are actually keywords in python
    # which are boolean value 
    print(a == b)
    print(a > b)
    print(a < b)
    
    c = True
    print(c, type(c), id(c))
    
    d = True
    print(d, type(d), id(d))
    
    print(c is d)
if __name__ == "__main__": main()