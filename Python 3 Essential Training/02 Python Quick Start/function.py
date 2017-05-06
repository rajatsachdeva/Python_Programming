#!/usr/bin/python3

# Functions 
# Program to detect if a number is prime

def isprime(num):
    if num == 1:
        print ("1 is special")
        return False
    for x in range(2, num):
        if 0 == num % x:
            print("{} equals {} x {}". format(num, x, num // x ))
            return False
    
    print(num, "is a prime number")
    return True

def main():
    for n in range(1, 20):
        result = isprime(n)
        
if __name__ == "__main__":
    main()