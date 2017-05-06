#!/usr/bin/python3

def main():
    a, b = 1, 1
    
    # Conditional Execution
    if a < b:
        print ("a is less than b")
    elif a > b:
        print ("a is greater than b")
    else:
        print ("a is equal to b")
        
    # Another form of conditionals in python
    # Conditional expression or conditional value 
    
    c ,d = 5, 6
    result = "less than" if c < d else "not less than"
    print (result)
if __name__ == "__main__":
     main()