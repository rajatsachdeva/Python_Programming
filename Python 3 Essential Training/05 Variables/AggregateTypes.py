#!/bin/python3

# Aggregate types

def main():
    print("In Aggregate Types")
    x = (1, 2, 3, 4, 5)
    
    # Python tries to print an object in the same form 
    # that is used to create it
    # tuples are immutable objects
    print(type(x), x)
    
    y = [1, 2, 3, 4, 5]
    
    # Python tries to print an object in the same form 
    # that is used to create it
    # Lists are mutable objects
    print(type(y), y)
    
    # Adding at the end of the list
    y.append(6)
    print(type(y), y)
    
    # insertion at a particular position
    y.insert(2, 9)
    print(type(y), y)
    
    # Another Aggregate/Sequence Type: Strings
    z = "string"
    print(type(z), z)
    # Strings are also immutable  
    # Subscript starts from 0 to length - 1     
    print(type(z), z[2])
    
    # Slicing
    # [start: end(not included): inrementor]
    print(z[2:4])
    print(z[1::2])
    print(z[:])
    
    for i in x:
        print(i)
        
      
if __name__ == "__main__": main()