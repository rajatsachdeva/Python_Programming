#!/bin/python3

# Finding 3rd party modules
# http://pypi.python.org/pypi

import bitstring

def main(): 
    a = bitstring.BitString(bin = '01010101')
    print(a.hex, a.bin, a.uint)
    
if __name__ == "__main__": main() 