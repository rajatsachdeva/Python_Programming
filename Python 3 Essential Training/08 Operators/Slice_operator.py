#!/usr/bin/python3

# Slice Operator

def main():
    print("Main Starts !")
    
    # declare a list
    list = []
    
    # Initialize
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
    
    print("list is = {}".format(list))

    print("list[0] = {}".format(list[0]))
    print("list[1] = {}".format(list[1]))
    print("list[4] = {}".format(list[4]))
    print("list[9] = {}".format(list[9]))
    
    # Overflow will give an Index out of range error
    # print("list[10] = {}".format(list[10]))
    
    # Slicing 
    # [ start : end[not included] : step size]
    print("list[0:5] = {}".format(list[0:5]))
    
    
    # Ranges in python are non-inclusive
    for i in range(0, 10):
        print(i, end= ' ')
    print()
    
    print(list[0:10])
    
    list[:] = range(100)
    print(list)
    
    print("list[27] = {}".format(list[27]))
    
    print("list[27:42] = {}".format(list[27:42]))
    print("list[27:42:3] = {}".format(list[27:42:3]))
    print("list[27:43:3] = {}".format(list[27:43:3]))
    
    # create an iterator
    for i in list[27: 43: 3]:
        print(i, end = ' ')
    print()
    
    list[27:43:3] = (99, 99, 99, 99, 99, 99)
    print(list)
    
if __name__ == "__main__": main()