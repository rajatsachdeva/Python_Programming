#!/usr/bin/python3

a, b = 5, 1

if a < b:
    print('a({}) is less than b ({})'.format(a,b))
else:
    print('a({}) is not less than b ({})'.format(a, b))
    
# In above example the format is used for print fromatting
# format is a method of a string object

# Conditional statement like in c
# print(a < b ? "foo": "bar")
print("foo" if a < b else "bar")