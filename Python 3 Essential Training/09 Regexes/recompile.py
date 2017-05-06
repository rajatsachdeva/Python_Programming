#!/usr/bin/python3

# Regular Expressions
# Very powerful method of matching patterns in text
# Actually a small language in itself, regexes can be very simple or very complex 

# Regular expression module
import re

def main():
    fh = open('raven.txt')
    # precompile the regular expression
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE) # can be written as re.I
    for line in fh:
        # search the pattern
        if re.search(pattern, line):
            print(pattern.sub('???', line), end = '')    

if __name__ == "__main__": main()
