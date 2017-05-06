#!/bin/python3

# Creating sequences with tuples and lists
# tuples and lists are basic array types in python

# tuples are immutable and created using (,) comma operator
# Lists are created with [] 
def main():
    t = 1, 2, 3, 4, 5
    print(t)
    print(type(t))
    print("t[0] = {}".format(t[0]))
    print("t[4] = {}".format(t[4]))
    print("t[-1] = {}".format(t[-1]))
    print("len(t) = {}".format(len(t)))
    print("min(t) = {}".format(min(t)))
    print("max(t) = {}".format(max(t)))
    
    t2 = (2, 3, 4, 4, 3, 2, 2)
    t3 = (1)
    print(t3, type(t3))
    
    # create a tuple with single element
    t3 = (1, )
    print(t3, type(t3))
    
    # lists
    l = [1,2, 3, 4, 5,8]
    print(l, type(l))
    
    print(l[0], l[-1], len(l), min(l), max(l))
    
    t = tuple(range(25))
    print(t)
    
    # tuples are immutable so cannot modidy the contents of a tuple
    # t[0] = 9 cannot perform this 
    
    # But same can be done for a list
    x = list(range(25))
    print(x,"\n", type(x))
    
    x [10] = 2222
    print(x)
if __name__ == "__main__": main()