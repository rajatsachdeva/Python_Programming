#!/usr/bin/python3

# Enumerate function in python
def main():
    fh = open('lines.txt')
    # enumerate function returns two values, which are 
    # index and value
    # index starts at 0
    for index, line in enumerate(fh.readlines()):
        print(index,line, end='')
    print()    
    s = 'this is a string'
    for i,ch in enumerate(s):
        print(i, ch)
        
    for i,ch in enumerate(s):
        if ch == 's': 
            print('index {} is an s'.format(i))
    
if __name__ == "__main__": main()
