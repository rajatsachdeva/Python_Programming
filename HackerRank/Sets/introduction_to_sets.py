'''
Created on 09-May-2017

@author: Rajat Sachdeva
'''
from __future__ import division

# 
# Sets are used to store unique items
#

def main():
    # Get Number of elements
    _ = int(raw_input())
    
    # Get the height of plants
    plants = map(int, raw_input().split())
    
    # Get the average of the unique heights
    res = average(plants)
    print res
    
def average(plants):
    # Convert the input into a set
    myset   = set(plants)
    hlen    = len(myset)
    hsum    = sum(myset)
    # Float Division
    return hsum / hlen 

if __name__ == '__main__':
    main()