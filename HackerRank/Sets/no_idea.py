'''
Created on 09-May-2017

@author: Rajat Sachdeva
'''

'''
There is an array of n integers. 
There are also 2 disjoint sets, A and B, each containing m integers. 
You like all the integers in set A and dislike all the integers in set B. 
Your initial happiness is 0. 
For each i integer in the array, if i belongs to A, you add 1 to your happiness. 
If i belongs to B, you add -1 to your happiness. Otherwise, your happiness does not change. 
Output your final happiness at the end.
'''
def main():
    # size n of input array and m for Sets A and B
    m, n = raw_input().split()
    # get the the input array from user
    input_arr = map(int, raw_input().split())
    A = set(map(int, raw_input().split()))
    B = set(map(int, raw_input().split()))
    get_happiness(input_arr, A, B)

def get_happiness(arr, a, b):
    print sum([(i in a) - (i in b) for i in arr])

if __name__ == '__main__':
    main()