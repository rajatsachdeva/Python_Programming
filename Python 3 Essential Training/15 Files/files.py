#!/usr/bin/python3

# Opening files in python

def main():
    # Open the file
    # gives the file handle object
    # it's an iterable object
    # it gives a line in iterable mode 
    # readlines() method is similar to this
    # modes : r: read, w: write, a: append 
    #, r+: read/write, rt: read text, rb: read binary
    # default mode is read mode
    f = open('lines.txt')
    for line in f:
        print(line, end = '')
    print()
    
    f2 = open('lines.txt', 'r')
    for line in f2.readlines():
        print(line, end = '')

if __name__ == "__main__": main()
