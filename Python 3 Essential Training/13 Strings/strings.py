#!/usr/bin/python3

# In python String are python
# String is an object and the variable containing the string is just a reference to a 
# string object

def main():
    
    s = 'this is a string1'
    print(s)
    # Upper case
    print(s.upper())
    print("This is a string2".upper())
    
    # format method 
    print("This is a string2 {}".format("621"))
    # % operator
    print("this is a string2 %d" % 42)
    
    # First letter capitalize
    print(s.capitalize())
    
    # lower case
    print(s.lower())
    
    # Title / Camel Case / First letter of each word is capitalize
    print(s.title())
    
    # Swap the cases from lower to upper and upper to lower
    s2 = "StrinGsssssSSS !"
    print(s2)
    print(s2.swapcase())
    
    # find a substring
    print(s.find('is'))
    
    # String Replace
    print(s.replace('this', 'that'))
    
    # id of an object
    print(id(s))
    
    newstring = s.upper()
    print(newstring)
    print(id(newstring))
    
    # strips the specific characters from start and end of the string
    # By Default it removes the whitespaces
    # commonly used to newlines
    print(s.strip())
    
    s3 = "     This is a string with whitespacess     "
    print(s3)
    print(s3.strip())
    
    # Right strip
    print(s3.rstrip())
    
    s4 = "this is a string with new line\n"
    print(s4)
    print(s4.rstrip('\n'))
    
    # left strip
    print(s3.lstrip())
    
    # Is Alpha Numeric
    print(s.isalnum()) # False: includes whitespaces
    s5 = "ThisisaString"
    print(s5.isalnum())
    
    # Is Alpha
    print(s.isalpha())
    
    # Is digit
    print(s.isdigit())
    
    # Is printable
    print(s.isprintable())
    
    #center
    s6 = "this is my new string"
    new = s.center(80)
    print(new)
    print(len(new))

if __name__ == "__main__": main()
