#!/usr/bin/python3

# Exception handling

# Exceptions are python's key method for handling errors.
# Whenever we see an error/Stack Trace , those error messages
# are nothing but simply uncaught exceptions.
# You can catch exceptions in python using try and except.

# You may raise your own exception with "raise"

def main():
    try:
        for line in readfile('lines.2txt'): 
            print(line.strip())
            # strip method strips/removes the trailing newline character
            # it's a string method 
    except IOError as e:
        print(e)
    except ValueError as e:
        print("Bad file format:",e)

def readfile(filename):
    if filename.endswith(".txt"):
        fh = open(filename)
        return fh.readlines()
    else:
        raise ValueError('Filename must end with .txt')
if __name__ == "__main__": main()
