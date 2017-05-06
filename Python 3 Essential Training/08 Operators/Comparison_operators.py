#!/usr/bin/python3

# Comparison Operators
   
def main():
    print("Main Starts !")
    
    print("5 <  6 = {}".format(5 <  6))
    print("6 <  5 = {}".format(6 <  5))
    print("5 <= 6 = {}".format(5 <= 6))
    print("5 <= 5 = {}".format(5 <= 5))
    
    print("6 >  5 = {}".format(6 >  5))
    print("6 >= 5 = {}".format(6 >= 5))
    print("6 >= 6 = {}".format(6 >= 6))
    print("6 >= 7 = {}".format(6 >= 7))
    
    print("6 == 6 = {}".format(6 == 6))
    print("5 == 6 = {}".format(5 == 6))
    
    print("6 != 6 = {}".format(6 != 6))
    print("5 != 6 = {}".format(5 != 6))
    
    x, y = 5, 6
    print("x = {} id(x) = {}\ny = {} id(y) = {}".format(x, id(x), y, id(y)))
    print("x is y = {}".format(x is y))
    print("x is not y = {}".format(x is not y))
    
    x, y = 5, 5
    print("x = {} id(x) = {}\ny = {} id(y) = {}".format(x, id(x), y, id(y)))
    print("x is y = {}".format(x is y))
    print("x is not y = {}".format(x is not y))
    
    # For immutables like integers, the ids are always going
    # to be same if value is same
    # So, testing Equality and testing id is almost the same thing
    
    # But for mutables
    # We need to test the values as they will have different id's 
    # As for mutables they will be different objects
    x, y = [5], [5]
    print("x = {} id(x) = {}\ny = {} id(y) = {}".format(x, id(x), y, id(y)))
    print("x is y = {}".format(x is y))
    print("x is not y = {}".format(x is not y))
    print("x == y = {}".format(x == y))
    print("x != y = {}".format(x != y))
     
if __name__ == "__main__": main()