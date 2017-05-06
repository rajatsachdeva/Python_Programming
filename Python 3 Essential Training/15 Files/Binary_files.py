#!/usr/bin/python3

# Reading and writing binary files in Python

def main():
    buffersize = 50000
    # Open the file
    inf = open('olives.jpg', 'rb')
    outf = open('olives_new.jpg', 'wb')
    
    # inf.read(size) is not an iterable so 
    # cannot use for loop
    buffer = inf.read(buffersize)
    while len(buffer):
        outf.write(buffer)
        print('.', end = '')
        buffer = inf.read(buffersize)
    print("\n Done")
if __name__ == "__main__": main()
