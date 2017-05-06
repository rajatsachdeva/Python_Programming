#!/bin/python3

# Dictionary or associate of Hash
# Muttable in nature
 
def main():
    print("Main Starts !")
    # key : value
    d = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5 }
    print(type(d), d)
    
    for key in sorted(d.keys()):
        print(key , d[key])
    print()
    # Another way of defining the dictonary objects
    
    d2 = dict(
        one = 1, two = 2, three = 3, four = 4, five = 'five'
    )
    
    for key in sorted(d2.keys()):
        print(key , d2[key])
    print()
        
    d['seven'] = 7
    for key in sorted(d.keys()):
        print(key , d[key])
    print()
if __name__ == "__main__": main()