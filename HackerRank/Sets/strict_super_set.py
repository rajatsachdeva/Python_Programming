'''
Created on 10-May-2017

@author: Rajat Sachdeva
'''
'''
You are given one set A and a number of other sets, N . 
Your job is to find whether set A is a strict superset of all the N sets. 
Print True, if A is a strict superset of all of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Example:
Set [1, 3, 4] is a strict superset of set [1, 3].
Set [1, 3, 4] is not a strict superset of set [1, 3, 4].
Set [1,3, 4] is not a strict superset of set [1, 3, 5].
'''
def main():
    A = set(raw_input().split())
    res = True
    for _ in range(int(raw_input())):
        B = set(raw_input().split())
        res = A.issuperset(B) and res
    print res
if __name__ == '__main__':
    main()