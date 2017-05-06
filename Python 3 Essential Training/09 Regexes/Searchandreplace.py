#!/usr/bin/python3

# Regular Expressions
# Very powerful method of matching patterns in text
# Actually a small language in itself, regexes can be very simple or very complex 

# Regular expression module
import re

def main():
    fh = open('raven.txt')
    for line in fh:
        # search the pattern
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(line.replace(match.group(), "###"), end = '')
            
#print(re.sub('(Len|Neverm)ore','###', line), end = '')
if __name__ == "__main__": main()
