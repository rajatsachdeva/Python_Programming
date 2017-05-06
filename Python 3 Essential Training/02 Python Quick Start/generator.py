#!/usr/bin/python3

# Generator Functions
# A generator is simply a function which returns an object on which you can call next, 
# such that for every call it returns some value, until it raises a StopIteration exception,
# signaling that all values have been generated. Such an object is called an iterator.
# Normal functions return a single value using return, just like in Java. 
# In Python, however, there is an alternative, called yield. 
# Using yield anywhere in a function makes it a generator

def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

# Generator function
def primes(n = 1):
   while(True):
       if isprime(n): yield n
       n += 1 

for n in primes():
    if n > 100: break
    print(n)

