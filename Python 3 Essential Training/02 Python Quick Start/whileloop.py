#!/usr/bin/python3

# simple fibonacci series
# the sum of two elements defines the next set
a, b = 0, 1
print (a, " ", end = "" )
while b < 50:
    print(b, " ", end ="")
    a, b = b, a + b
    # Similar to write
    # c = a + b
    # a = b
    # b = c
