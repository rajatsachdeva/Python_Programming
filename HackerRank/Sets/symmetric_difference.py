'''
Created on 09-May-2017

@author: Rajat Sachdeva
'''
'''
Task 
Given  sets of integers, M and N, 
print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

Symmetric difference |A - B| = (A - B) U (B - A)

Input Format

The first line of input contains an integer, . 
The second line contains  space-separated integers. 
The third line contains an integer, . 
The fourth line contains  space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.
'''

def main():
    # get the two set from user
    _ = raw_input() # Number of elements in set A
    # Get the Set A
    A = set(map(int, raw_input().split()))
    _ = raw_input() # Number of elements in set B
    # Get the Set B
    B = set(map(int, raw_input().split()))
    
    # Get Absoulte Difference
    for i in sorted(abs_diff(A, B)):
        print i        
    
def abs_diff(a, b):
    a_minus_b = a.difference(b)
    b_minus_a = b.difference(a)
    return a_minus_b.union(b_minus_a)
    
if __name__ == '__main__':
    main()