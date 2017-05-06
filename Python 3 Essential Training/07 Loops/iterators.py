#!/usr/bin/python3

# Iterators in python
# So the readlines method inside the file object is called an iterator
# it takes one object at a time from a sequence of objects, and it returns
# one at a time
def main():
    fh = open('lines.txt')
    # fh.readlines() is actually the iterator here
    for line in fh.readlines():
        print(line, end = '')
    print()
    
    # In Python all container types are iterators
    for i in [1, 2, 3, 4, 5]:
        print(i, end= ' ')
    print()

    # In Python all container types are iterators
    for i in "string":
        print(i, end= ' ')
    print()
    
    for i in "string":
        print(i)
    print()

if __name__ == "__main__": main()
