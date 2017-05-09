'''
Created on 09-May-2017

@author: Rajat Sachdeva
'''
from __future__ import print_function

'''
print 1...N
inclusive range
'''

def main():
    n = int(raw_input())
    for i in range(1,n+1):
        print(i, end='')
        
if __name__ == '__main__':
    main()