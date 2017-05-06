# Functions

# define a function
def func1():
    print "I am a function"

# function that takes arguments
def func2(arg1, arg2):
    print arg1, " ", arg2


# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def power(num, x=1):
    result = 1;
    for i in range(x):
        result = result * num  
    return result

#function with variable number of arguments
# *args is variable arguments
def multi_add(*args):
    result = 0;
    for x in args:
        result = result + x
    return result

func1()
print func1()
'''
    this firsts call the function func1() and prints the output
    but now as the func1 does not return any value, so 'None' is printed 
'''
print func1      
# This gives the address of the of the function func1
#Functions itself are objects in python and have some address

#Functions with Arguments
func2(10,20)
print func2(10,20)

#Print the function which is returning some value
print "cube value %d" %cube(3)

# Giving only the value for num 
# x is taken as 1 which is the default value here
print power(2)

# Giving both the arguments with some value 
print power(2,3)

# Giving positional parameters 
print power(x=3, num=2)

# Gives the list of input parameters in functions 
print multi_add(4,5,10,4)
