'''
Created on 09-May-2017

@author: Rajat Sachdeva
'''

'''
If the inputs are given on one line separated by a space character, 
use split() to get the separate values in the form of a list:

>> a = raw_input()
5 4 3 2
>> lis = a.split()
>> print (lis)
['5', '4', '3', '2']
If the list values are all integer types, use the map() method to convert all the strings to integers.

>> newlis = list(map(int, lis))
>> print (newlis)
[5, 4, 3, 2]
Sets are an unordered bag of unique values. A single set contains values of any immutable data type. 

'''
def main():
    # CREATING SETS
    myset = {1, 2} # Directly assigning values to a set
    print myset
    myset = set()  # Initializing a set
    myset = set(['a', 'b']) # Creating a set from a list
    print myset
    
    # MODIFYING SETS
    # Using the add() function:
    myset.add('c')
    print myset

    myset.add('a') # As 'a' already exists in the set, nothing happens
    print myset
    myset.add((5, 4)) # add a tuple
    print myset
    
    # Using the update() function:
    myset.update([1, 2, 3, 4]) # update() only works for iterable objects
    print myset

    myset.update({1, 7, 8})
    print myset
    myset.update({1, 6}, [5, 13])
    print myset

    # REMOVING ITEMS 
    # Both the discard() and remove() functions take a single value as an argument 
    # and removes that value from the set. If that value is not present, discard() does nothing, 
    # but remove() will raise a KeyError exception.

    myset.discard(10)
    print myset
    
    myset.remove(13)
    print myset

    # COMMON SET OPERATIONS 
    # Using union(), intersection() and difference() functions. 

    a = {2, 4, 5, 9}
    b = {2, 4, 11, 12}
    print a
    print b
    # Union
    print a.union(b) # Values which exist in a or b
    # intersection
    print a.intersection(b) # Values which exist in a and b
    # difference
    print a.difference(b) # Values which exist in a but not in b

    # The union() and intersection() functions are symmetric methods: 
    print a.union(b) == b.union(a)
    print a.intersection(b) == b.intersection(a)
    print a.difference(b) == b.difference(a)

if __name__ == '__main__':
    main()