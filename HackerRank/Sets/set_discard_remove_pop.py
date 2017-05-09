'''
Created on 09-May-2017

@author: Rajat Sachdeva
'''
'''
remove(x)
This operation removes element x from the set. 
If element  does not exist, it raises a KeyError.
The .remove(x) operation returns None.

Example

>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.remove(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.remove(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.remove(0)
KeyError: 0

.discard(x)
This operation also removes element  from the set. 
If element  does not exist, it does not raise a KeyError.
The .discard(x) operation returns None.

Example

>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.discard(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.discard(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.discard(0)
>>> print s
set([1, 2, 3, 6, 7, 8, 9])

.pop()
This operation removes and return an arbitrary element from the set. 
If there are no elements to remove, it raises a KeyError.

Example

>>> s = set([1])
>>> print s.pop()
1
>>> print s
set([])
>>> print s.pop()
KeyError: pop from an empty set
'''

def main():
    _ = raw_input()
    s = set(map(int, raw_input().split()))
    N = int(raw_input()) 
    for _ in range(N):
        set_operations(s)
    print sum(s)
        
def set_operations(s):
    request_str = raw_input().split(' ')        
    command = request_str[0]
    
    # check which operations to perform
    if command == 'discard':
        val = int(request_str[1])
        s.discard(val)
    elif command == 'remove':
        val = int(request_str[1])
        s.remove(val)
    elif command == 'pop':
        s.pop()
    else:
        print "incorrect operation"

if __name__ == '__main__':
    main()