'''
Created on 09-May-2017

@author: Rajat Sachdeva
'''
from __future__ import division

def main():
    a = int(raw_input())
    b = int(raw_input())
    # Integer Division
    print a // b
    # Float Division
    print a / b

def test():
    input_a = range(10)
    input_b = range(10)
    for a in input_a:
        for b in input_b:
            try:
                print a, '/', b, '=',a / b
            except Exception as e:
                print e
if __name__ == '__main__':
    test()