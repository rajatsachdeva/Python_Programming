'''
Created on 09-May-2017

@author: Rajat Sachdeva
'''
'''
We have seen the applications of union, intersection, difference and symmetric difference operations, 
but these operations do not make any changes or mutations to the set.

We can use the following operations to create mutations to a set:

.update() or |= 
Update the set by adding elements from an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
.intersection_update() or &=
Update the set by keeping only the elements found in it and an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])
.difference_update() or -=
Update the set by removing elements found in an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])
.symmetric_difference_update() or ^=
Update the set by only keeping the elements found in either set, but not in both.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])
TASK
You are given a set  and  number of other sets.
These  number of sets have to perform some specific mutation operations on set .
Your task is to execute those operations and print the sum of elements from set .
'''

def main():
    # Get the number of elements in Set A
    # and the Set A
    (_, A) = (raw_input(), set(map(int, raw_input().split())))
    # Get the number of instructions to be executed
    for _ in xrange(input()):
        # Get the command to be executed 
        # Get the set argument
        (command, newSet) = (raw_input().split()[0], set(map(int, raw_input().split())))
        # execute the command
        getattr(A, command)(newSet)
        
    print str(sum(A))
    
if __name__ == '__main__':
    main()