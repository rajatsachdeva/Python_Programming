'''
Created on 09-May-2017

@author: Rajat Sachdeva
'''
from __future__ import print_function
'''
Let's learn about list comprehensions! 
You are given three integers  x, y and z representing the dimensions of a cuboid along with an integer N. 
You have to print a list of all possible coordinates given by i, j ,k on a 3D grid 
where the sum of x , y and z is not equal to N.
Here:
0 <= i <= x
0 <= j <= y
0 <= k <= z
'''
def main():
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    print ([[a , b , c] for a in range(0, x+1) for b in range(0,y+1) for c in range(0, z+1) if a+b+c != n])
if __name__ == '__main__':
    main()