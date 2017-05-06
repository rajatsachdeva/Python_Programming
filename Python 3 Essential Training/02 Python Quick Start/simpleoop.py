#!/usr/bin/python3

# Classes - definition to create an object
# Objects are instances of Classes

# simple fibonacci series
# the sum of two elements defines the next set
class Fibonacci():
    # self is reference to object
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # generator
    def series(self):
        while(True):
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b

# Creating an instance(object) of class
# objectname = classname(args)
f = Fibonacci(0, 1) # init is called here
for r in f.series():
    if r > 100: break    
    print(r, end=' ')

