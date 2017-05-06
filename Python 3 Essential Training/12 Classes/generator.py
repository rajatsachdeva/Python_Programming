#!/usr/bin/python3

# A generator object is an object that can be used in the context of an iterable
# like in for loop

# Create own range object with inclusive range
class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        if numargs < 1 : 
            raise TypeError('Requries at least one argument')
        elif numargs == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        elif numargs == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else:
            raise TypeError('Number of arguments should be 3, but they are {}'.format(numargs))
        
    # Generator
    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step
            
def main():
    # generator object
    o = range(0, 25, 1) # start, stop
    for i in o: print(i, end = ' ')
    print()
    mygen = inclusive_range(1,18)
    for i in mygen: print(i, end = ' ')
    print()
    for i in inclusive_range(10): print (i , end = ' ')

if __name__ == "__main__": main()