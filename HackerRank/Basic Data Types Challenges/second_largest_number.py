'''
Created on 09-May-2017

@author: Rajat Sachdeva
'''

'''
You are given N numbers. Store them in a list and find the second largest number.
'''

def main():
    # Get Number of elements
    N = raw_input()
    l = map(int, raw_input().split())
    top = max(l)
    while top == max(l):
        l.remove(top)
    print(max(l))
    
if __name__ == "__main__": main()