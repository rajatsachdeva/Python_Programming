'''
Created on 09-May-2017

@author: Rajat Sachdeva
'''
from __future__ import print_function
def main():
    # Take input from User
    n = int(raw_input())
    print_result(n)

def print_result(num):
    # check if num is odd
    if num % 2 != 0:
        print ('Weird')
    # else num is even    
    elif num in range(2,6):
        print ('Not Weird')
    elif num in range(6,21):
        print ('Weird')
    elif num > 20:
        print ('Not Weird')
    else:
        print('Invalid')

def test():
    mycases = range(0, 30)
    for i in mycases:
        print(i, end =' ')
        print_result(i)
        
if __name__ == '__main__': test()