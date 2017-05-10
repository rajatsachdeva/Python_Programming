'''
Created on 10-May-2017

@author: Rajat Sachdeva
'''

from __future__ import print_function

'''
logic:

K members per group

get the unique number of rooms
let say r1 r2 r3... cR (crR for captain) ---- (1)

input list will be:
let say kr1 kr2 kr3... cR (crR for captain) ------(2)

multiply (1) by k
we get kr1 kr2 kr3... kcR -------(3)

get sum of (3) and sum of (2)

sum(3) = kr1 + kr2 + kr3... + kcr
sum(2) = kr1 + kr2 + kr3... + cR

subtract both the sums
sum(3) - sum(2) = (k - 1) cR
cR = (sum(3) - sum(2)) / (k - 1)

'''


def main():
    # get the value of K, Number of members per group
    k = int(raw_input())
    # list of room numbers
    l = map(int, raw_input().split())
    myset = set(l)
    print(((sum(myset) * k) - (sum(l)))/ (k -1))
if __name__ == '__main__':
    main()