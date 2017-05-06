#!/usr/bin/python3

# In python String are python
# String is an object and the variable containing the string is just a reference to a 
# string object

# Spliting and Joining Strings

def main():
    s = 'This is a string of words'
    print(s)
    print("Split the string")
    print(s.split())
    
    print()
    
    s2 = 'This is a string of                         words'
    print(s2)
    print("Split the string")
    print(s.split())
    
    # Does not split on whitespaces
    print(s.split('i'))
    words = s.split('i')
    for w in words: print(w)
    
    # join the words
    new = ':'.join(words)
    print("\n", new)
    
    new = 'x'.join(words)
    print("\n", new)
    
if __name__ == "__main__" : main()