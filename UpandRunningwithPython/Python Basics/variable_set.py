#
# File for Varirables
#

# Declare a variable and initizalize it
f = 0
print f

# re-declaring the variable works
#f = "abc"
#print f

# ERROR: variables of different types cannot be combined
#print "string type " + 123
#Python is a strongly typed language
#print "string type " + str(123)


# Global vs. local variables in functions
def someFunction():
    global f
    f = "def"
    print f

someFunction()
print f 

del f
#print f
#throws error as the variable is deleted and does not exists

