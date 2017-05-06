#!/usr/bin/python3

# Organizing data with dictionaries

def main():
    d1 = {'one' : 1, 'two' : 2, 'three' : 3}
    print(d1, type(d1))
    
    # dictionary using dict constructor 
    d2 = dict(one = 1, two = 2, three = 3)
    print(d2, type(d2))
    
    d3 = dict(four = 4, five = 5, six = 6)
    print(d3, type(d3))
    
    # Using keyword arguments
    # ** this denots the kwargs 
    d4 = dict(one = 1, two = 2, three = 3, **d3)
    print(d4, type(d4))
    
    # check if a value is in dictionary
    print('four' in d3)
    print('three' in d3)
    
    # Iterate over dict elements
    # to print all the keys
    for key in d4: 
        print(key, end = ' ')
    print()
    
    # Iterate over dict elements to print all the keys and values
    for key,value in d4.items(): 
        print(key, "=", value)
    print()
    
    # Get a particular item from a dictionary
    print("d4['three'] =", d4['three'])
    
    # get method to get a value for a key from a dict object
    print(d3.get('three'))
    print(d4.get('three'))
    # Set a default return value in case key is not present
    print(d3.get('three', 'Not Found'))
    
    # delete an item from a dict
    del d3['four']
    print(d3, type(d3))
    
    # pop an item from a dict
    # In dictionary it requires atleast one argument
    d3.pop('five')
    print(d3, type(d3))
     
if __name__ == "__main__": main()
