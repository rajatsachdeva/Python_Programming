#!/usr/bin/python3

# Bitwise operations

# function to print in binary format
def b(num): print('{:08b}'.format(num))

def main():
    print("Main Starts !")
    print(5)
    print(0b0101)
    
    # Use binary function
    b(5)
    x, y = 0x55, 0xaa
    print("x = {}".format(x))
    print("y = {}".format(y))
    b(x)
    b(y)
    b(x | y)
    b(x & y)
    b(x ^ y)
    b(x ^ 0)
    b(x ^ 0xff)
    b(x << 4)
    b(x >> 4)
    b(~ x)
    
if __name__ == "__main__": main()