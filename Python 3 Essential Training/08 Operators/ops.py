#!/usr/bin/python3
# Simple Arithmetic

def main():
    print("Main Starts !")
    
    res = 5 + 5
    print("5 + 5 = {}".format(res))
    res = 5 * 5
    print("5 * 5 = {}".format(res))
    res = 5 - 3 
    print("5 - 3 = {}".format(res))
    res = 5 / 3
    print("5 / 3 = {}".format(res))
    
    # Floor Division or Integer Division
    res = 5 // 3
    print("5 // 3 = {}".format(res))
    
    res = 5 % 3
    print("5 % 3 = {}".format(res))
    
    # divmod to get divisor and remainder together
    div, rem = divmod(5, 3)
    print("5 // 3 = {}\n5 % 3 = {}".format(div, rem))
    
    # Increment/Decrement operator
    num = 5
    print("num = {}".format(num))
    num += 1
    print("num = {}".format(num))
    num -= 1
    print("num = {}".format(num))
    num *= 5
    print("num = {}".format(num))
    num //= 5
    print("num = {}".format(num))
            
if __name__ == "__main__": main()
