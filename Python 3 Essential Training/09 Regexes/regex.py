#!/usr/bin/python3

# Regular Expressions
# Very powerful method of matching patterns in text
# Actually a small language in itself, regexes can be very simple or very complex 

# Regular expression module
import re

def main():
    fh = open('raven.txt')
#    for line in fh:
#        # search the pattern
#        if re.search('(Len|Neverm)ore', line):
#            print(line, end='')

    for line in fh:
        match = re.search('(Len|Neverm)ore', line)
        # search the pattern
        if match:
            print(match.group())

if __name__ == "__main__": main()
