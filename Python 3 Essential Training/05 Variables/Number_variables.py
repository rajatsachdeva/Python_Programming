#!/bin/python3

# There are two types of numbers in python

def main():
    print("main starts")
    
    # Integer
    num1 = 42
    print(num1,type(num1))
    
    # Floating point number
    num2 = 42.0
    print(num2, type(num2))
    
    # Division in Python 3
    div_result = 42 / 9 
    print("Division:", div_result, type(div_result))
    
    # Rounding the result
    print("Rounded Result:", round(div_result, 2))
    
    # Integer Division 
    div_result2 = 42 // 9 
    print("Integer Division:", div_result2, type(div_result2))
    
    # Remainder
    rem = 42 % 9 
    print("Remainder:", rem, type(rem))
    
    # Type Casting
    num3 = int(42.9)
    print("result:", num3, type(num3))
    
     # Type Casting
    num4 = float(42)
    print("result:", num4, type(num4))
    
    # float and int are actually object constructors
    
if __name__ == "__main__": main()