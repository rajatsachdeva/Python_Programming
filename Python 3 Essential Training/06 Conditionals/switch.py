#!/usr/bin/python3

# Switch
# How to create a switch statement in python
def main():
    print('Main Starts')
    # declare a dictionary
    choices = dict(
        one = "first",
        two = "second",
        three = "third",
        four = "fourth",
        five = "fifth"
    )
    
    v1 = "three"
    print(choices[v1])
    v2 = "seven"
    # using get method of dict with default result
    print(choices.get(v2, 'other'))
if __name__ == "__main__": main()
