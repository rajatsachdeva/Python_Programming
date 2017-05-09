'''
Created on 09-May-2017

@author: Rajat Sachdeva
'''
def main():
    # Get number of elements from user
    n = int(raw_input())
    # Get elements from user
    # Create a list of those input elements
    integer_list = map(int, raw_input().split())
    
    # convert the list to tuple 
    t = tuple(integer_list)
    
    #compute hash of elements
    print hash(t)
    
    
if __name__ == '__main__':
    main()