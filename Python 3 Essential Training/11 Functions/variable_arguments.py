#!/usr/bin/python3

# Functions in Python
# Variable Arguments
# list of things

def main():
    testfunc(1, 2, 3, 42, 43, 45, 46)

# Function with variable number of arguments
def testfunc(this , that, other, *args):
    print(this, that , other, args)
    # args is tuple of all the values passed to function
  
    # It's a tuple so can only read the data not update the same  
    for i in args:
        print (i, end = ' ')
        
    print (args[1])
    
if __name__ == "__main__": main()