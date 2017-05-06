#!/usr/bin/python3

# Opening files in python

def main():
    infile = open('lines.txt', 'r')
    outfile = open('new.txt', 'w')
    # Wirte to new file
    for line in infile:
        print(line, file = outfile, end = '')
    print('Done.')
    
    # How to copy large files
    # Buffer mode
    buffersize = 50000 # bytes
    
    infile1 = open('bigfile.txt', 'r')
    outfile1 = open('new2.txt', 'w')
    
    buffer = infile1.read(buffersize)
    # Wirte to new file
    while(len(buffer)):
        outfile1.write(buffer)
        print('.', end = '')
        buffer = infile1.read(buffersize)
    print('\nDone.')
    
if __name__ == "__main__": main()
