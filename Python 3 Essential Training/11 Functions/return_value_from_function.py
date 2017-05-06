#!/usr/bin/python3

# Functions in Python

# Use of return keyword in Python

def main():
    print(testfunc())
    print(mytestfunc())
    for i in mytestfunc(): print(i , end= ' ')
    
def testfunc():
    return 'This is a test function'
    
# Return object from function
def mytestfunc():
    return range(25)

if __name__ == "__main__": main()
