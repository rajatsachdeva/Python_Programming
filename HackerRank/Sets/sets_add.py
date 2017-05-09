'''
Created on 09-May-2017

@author: Rajat Sachdeva
'''
'''
If we want to add a single element to an existing set, we can use the .add() operation. 
It adds the element to the set and returns 'None'.

>>> s = set('HackerRank')
>>> s.add('H')
>>> print s
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
>>> print s.add('HackerRank')
None
>>> print s
set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])
'''
def main():
    # Get number of inputs from user
    n = int(raw_input())
    # create a set of stamps
    stamps = set()
    # Get the stamp names from user
    for _ in range(n):
        stamps.add(raw_input())
    print len(stamps)
    
if __name__ == '__main__':
    main()