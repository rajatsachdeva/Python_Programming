'''
Created on 10-May-2017

@author: Rajat Sachdeva
'''
'''
You are given two sets, A and B. 
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

'''

def main():
    for _ in range(int(raw_input())):
        (_, A) = (raw_input(), set(raw_input().split()))
        (_, B) = (raw_input(), set(raw_input().split()))
        print A.issubset(B)
if __name__ == '__main__':
    main()