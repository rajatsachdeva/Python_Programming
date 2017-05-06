#!/usr/bin/python3

# Boolean Operators
   
def main():
    print("Main Starts !")
    
    print("7 < 5 = {}".format(7 < 5))
    print("5 == 5 = {}".format(5 == 5))
    
    print("type(True) = {}".format(type(True)))
    
    print("True and False = {}".format(True and False))
    print("True and True = {}".format(True and True))
    
    print("True or False = {}".format(True or False))
    print("True or True = {}".format(True or True))
    print("False or False = {}".format(False or False))
    
    # Bitwise Operation
    # this different from the logical boolean operation
    print("True & True = {}".format(True & True))
    
    a, b = 0, 1
    x, y = 'zero', 'one'
    
    print("a < b = {}".format(a < b))
    print("x < y = {}".format(x < y))
    
    if a < b and x < y:
        print("yes")
    else:
        print("no")
    
if __name__ == "__main__": main()