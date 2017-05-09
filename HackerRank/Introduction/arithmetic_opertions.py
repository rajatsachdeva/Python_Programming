'''
Created on 09-May-2017

@author: Rajat Sachdeva
'''

def main():
    a = int(raw_input())
    b = int(raw_input())
    print_result(a, b)
    
def print_result(a, b):
    print a + b
    print a - b
    print a * b

def test():
    inputs = ((1,2), (3,5), (6,7))
    for (a,b) in inputs:
        print_result(a, b)

if __name__ == '__main__':
    test()