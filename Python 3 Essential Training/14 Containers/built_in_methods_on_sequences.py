#!/bin/python3

# Built in methods on lists and tuples
# can perform any operation in tuple that will not modify the contents of the tuple
def main():
    t = tuple(range(25))
    print(t)
    print(type(t))
    print(10 in t)
    print(50 in t)
    print(50 not in t)
    print(t[10])
    print(len(t))
    
    for i in t: print(i, end = ' ')
    print()
    
    x = list(range(20))
    print(x)
    print(type(x))
    print(10 in x)
    print(20 in x)
    print(20 not in x)
    print(x[10])
    print(len(x))
    
    for i in x: print(i, end = ' ')
    print()
    
    x[10] = 222
    for i in x: print(i, end = ' ')
    print()
    
    # Count number of 5's in a tuple
    print(t.count(5))
    print(x.count(5))
    
    # Index of first occurence of 5
    print(t.index(5))
    print(x.index(5))
    
    # Tuple has no attribute append
    # t.append(100)
    x.append(100)
    print(x)
    print(len(x))
    
    # extend a list
    x.extend(range(21,30))
    print(x)
    
    # insert in a list
    # position, value
    x.insert(0, 25)
    x.insert(12, 100)
    print(x)
    
    # Remove a value from a list
    # Removes the first occurrence of the input value
    x.remove(12)
    print(x)
    
    # To delete a value at a particular position use del operator
    del x[12]
    print(x)
    
    # pop is used to  remove elements from the end
    x.pop()
    print(x)
    
    # pop from begining
    x.pop(0)
    print(x)
    
if __name__ == "__main__":
    main()