#!/bin/python3

# Strings in Python are immutabe objects 
# they are create using " " or ' '

# Escape character are similar to other languages

def main():
    s = "This is a string"
    print("String:", s, " Type:", type(s))
    
    # Escape characters
    s2 = "This is a\n string"
    print(s2)
    
    # Raw strings   
    # mostly used in regular expressions
    s3 = r"This is a\n Raw string"
    print(s3)
    
    # Formatting
    # Using format method of string class/object
    # python 3 only 
    n = 42
    s4 = "This is a {} string!".format(n)
    print(s4)
    
    # python 2 way
    s5 = "This is a %s string!" % n
    print(s5)

    # Using triple quotes to have strings that span multiple lines
    # '''\ this helps to remove the extra blank line whenever entering the text in 
    # multiple lines
    # It adds the text in the same form as the text in written in the python file
    s6 = '''\
This is a string 
line after line 
of text and more
text.'''
    print(s6)
if __name__ == "__main__": main()