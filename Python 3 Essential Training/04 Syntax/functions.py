#!/bin/python3

def main():
    # Call the function
    func1()
    func1()
    func2(2)
    func2(5)
    func2(7)
    func2() # default argument

# Define a function
def func1():
    for i in range(10):
        print(i, end= ' ')
    # print a newline
    print()

# Define a function
def func2(a = 8):
    for i in range(a , 10):
        print(i, end= ' ')
    # print a newline
    print()

    
if __name__ == "__main__":
    main()