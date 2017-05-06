#!/usr/bin/python3

# Generator functions

def main():
    for i in inclusive_range(0, 10):
        print(i, end = ' ')
    print()
    for i in inclusive_range2(18):
        print(i, end = ' ')
    print()
    for i in inclusive_range2(0, 25):
        print(i, end = ' ')
    print()
    for i in inclusive_range2(0, 50, 2):
        print(i, end = ' ')
    print()
    for i in inclusive_range2(7, 50, 2):
        print(i, end = ' ')
    print()
         
def inclusive_range(start = 0, stop = 0, step = 1):
    i = start
    while i <= stop:
        # You can return the value 
        # using yield
        yield i 
        i += step
               
def inclusive_range2(*args):
    numargs = len(args)
    if numargs < 1: 
        raise TypeError("requires atleast one argument")
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError("inclusive_range expected at most 3 arguments, got {}".format(numargs))
    
    i = start
    while i <= stop:
        yield i
        i += step
        
if __name__ == "__main__": main()

# yield returns each time the next item in the sequence.