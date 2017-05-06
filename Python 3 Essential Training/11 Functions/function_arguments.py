#!/usr/bin/python3

# Functions in Python

# Named/Keyword Arguments in python

def main():
    testfunc(5, 6, 7, 8, 9, 'ss', one = 1, two = 2, four = 52)
    testfunc2(one = 1, two = 2, four = 52)
    
# Function with named arguments
# **kwargs, keyword args
def testfunc(n1, n2 , n3 , *args, **kwargs):
    print(n1, n2 , n3 , args)
    for i in args:
        print (i, end = ' ')
    print()
    print(kwargs['one'], kwargs['two'], kwargs['four'])
    
def testfunc2(**kwargs):
    for k in kwargs:
        print(k , kwargs[k])
         
if __name__ == "__main__": main()