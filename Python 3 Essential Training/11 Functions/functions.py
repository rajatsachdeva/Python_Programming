#!/usr/bin/python3

# Functions in Python

def main():
    testfunc()
    mytestfunc()
    testfunc2(2)
    testfunc3(3)
    testfunc3(3, 4, 5)
    testfunc3(3, 4, 5, 1)
    
def testfunc():
    print('This is a test function')
    
# funtion with no body
# we can add a temp statement 'pass'
# pass is used to do nothing
def mytestfunc():
    pass

# Function with arguments
def testfunc2(number):
    print('This is test function',number)
    
# Function with default arguments
# None is a special value that we can test for
def testfunc3(num1, num2 = 0, num3 = 0, num4 = None):
    if num4 == None:
        num4 = 10
    print('This is test function',num1, num2, num3, num4)

if __name__ == "__main__": main()
