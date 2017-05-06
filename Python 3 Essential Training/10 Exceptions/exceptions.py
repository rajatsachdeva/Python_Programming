#!/usr/bin/python3

# Exception handling

# Exceptions are python's key method for handling errors.
# Whenever we see an error/Stack Trace , those error messages
# are nothing but simply uncaught exceptions.
# You can catch exceptions in python using try and except.

# You may raise your own exception with "raise"

def main():
    try:
        fh = open('lines.txt')
        for line in fh: print(line.strip())
        # strip method strips/removes the trailing newline character
        # it's a string method 
    except IOError as e:
        print(e)
    
    try:
        fh2 = open("lines2.txt")
    except IOError as e:
        print(e)
        print("could not open the file. come back tomorrow")
    else:
        for i in fh2 : print(i)
if __name__ == "__main__": main()
