# Remove the smallest element from the set, s. If  the set is empty, it remains empty.

# A Set is defined/created by placing the elements inside curly braces {} which are separated by comma.
# using pop() method on a set variable we are able to remove the lowest element from the set and if set is empty nothing is done
# Same is shown below with example

>>> s = {1, 2, 3, 4, 5}
>>> print(s)
{1, 2, 3, 4, 5}

>>> type(s)
<class 'set'>
>>> s.pop()
1
>>> print(s)
{2, 3, 4, 5}
>>> s.pop()
2
>>> s.pop()
3
>>> print(s)
{4, 5}
>>> s.pop()
4
>>> print(s)
{5}
>>> s.pop()
5
>>> print(s)
set()
>>> 

>>> s = {1}
>>> type(s)
<class 'set'>
>>> s.pop()
1
>>> print(s)
set()
>>> s.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'pop from an empty set'
>>> 

## Given that s has been defined, and that the_set that refers to a set, 
## write an expression that whose value is True if and only if the value to which s refers is in the_set.

# Here we will use 'in' operator to check if 's' is present in 'the_set' or not. Same is shown below with example.

>>> the_set = {5, 2, 1, 3, 4}
>>> print(the_set)
{1, 2, 3, 4, 5}
>>> s = 5
>>> s in the_set
True
>>> s = 6
>>> s in the_set
False
>>> 