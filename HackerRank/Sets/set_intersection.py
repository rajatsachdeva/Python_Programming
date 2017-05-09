'''
Created on 09-May-2017

@author: Rajat Sachdeva
'''

'''
.intersection()
The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.
The set is immutable to the .intersection() operation (or & operation).

>>> s = set("Hacker")
>>> print s.intersection("Rank")
set(['a', 'k'])

>>> print s.intersection(set(['R', 'a', 'n', 'k']))
set(['a', 'k'])

>>> print s.intersection(['R', 'a', 'n', 'k'])
set(['a', 'k'])

>>> print s.intersection(enumerate(['R', 'a', 'n', 'k']))
set([])

>>> print s.intersection({"Rank":1})
set([])

>>> s & set("Rank")
set(['a', 'k'])
The students of District College have subscriptions to English and French newspapers. 
Some students have subscribed only to English, some have subscribed only to French, 
and some have subscribed to both newspapers.
You are given two sets of student roll numbers. 
One set has subscribed to the English newspaper, 
one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to both newspapers.
'''

def main():
    _ = raw_input()
    eng = set(map(int, raw_input().split()))
    _ = raw_input()
    frn = set(map(int, raw_input().split()))
    total = len(eng.intersection(frn))
    print total

if __name__ == '__main__':
    main()