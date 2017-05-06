#!/usr/bin/python3

def main():
    for n in primes(): # Generate a list of prime number 
        if n > 100: break
        print(n)

def isprime(n):
    if n == 1:  # 1 is never prime 
        return False
    for x in range(2, n):
        if n % x == 0: # found a divisor, not prime 
            return False
    else:
        return True

def primes(n = 1): # generator Function
   while(True):
       if isprime(n): yield n # yield makes this a generator
       n += 1 

if __name__ == "__main__": main()
