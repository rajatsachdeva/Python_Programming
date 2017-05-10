'''
Created on 09-May-2017

@author: Rajat Sachdeva

'''
from __future__ import print_function
'''
Use of _ in loops
It's just a variable name, and it's conventional in python to use _ for throwaway variables. 
It just indicates that the loop variable isn't actually used.
'''

def main():
    marksheet = []
    for _ in range(0,int(raw_input())):
        marksheet.append([raw_input(), float(raw_input())])
    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
    
if __name__ == '__main__':
    main()