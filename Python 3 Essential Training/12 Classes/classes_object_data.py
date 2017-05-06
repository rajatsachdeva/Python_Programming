#!/usr/bin/python3

# Classes in python
# Using object data

# Should keep the access to data local to class 
# should only be set/get using class methods  

# Use accessor methods 
# Encapsulation

# define a class
class Duck:
    def __init__(self, color = 'white'):
        self._color = color
        
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
      
    def get_color(self):
        return self._color
    
    def set_color(self, color):
        self._color = color

# define a class
class Dog:
    # Keyword arguments helps us scale 
    def __init__(self, **kwargs):
        # Default name Tod
        self._name = kwargs.get('name', 'Tod')
        
    def bark(self):
        print('Woof!')

    def walk(self):
        print('Walks like a Dog.')
      
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

# define a class
class Cat:
    # Keyword arguments helps us scale 
    def __init__(self, **kwargs):
        # Default name snuggle
        self.variables = kwargs
        
    def Sound(self):
        print('Meow!')

    def walk(self):
        print('Walks like a Cat.')
      
    def get_name(self):
        return self.variables.get('name', None)
    
    def set_name(self, name):
        self.variables['name'] = name
        
    def set_variables(self, k , v):
        self.variables[k] = v
    
    def get_variables(self, k):
        return self.variables.get(k, None)
        
def main():
    # create an Instance/object of Duck class
    donald = Duck()
    print(donald)
    donald.quack()
    donald.walk()
    print(donald.get_color())
    donald.set_color('Red')
    print(donald.get_color())
    
    # Create a Dog object
    scooby = Dog(feet = 4)
    scooby.bark()
    scooby.walk()
    print(scooby.get_name())
    scooby.set_name("Spot")
    print(scooby.get_name())
    
    # Create a cat object
    cat1 = Cat()
    cat2 = Cat(name = 'snuggles', feet = 4)
    print(cat1.get_name())
    print(cat2.get_name())
    print(cat1.get_variables('name'))
    print(cat2.get_variables('name'))
    print(cat2.get_variables('feet'))
    
    cat1.set_variables('name', 'bubbles')
    cat1.set_variables('feet', '3')
    print(cat1.get_variables('name'))
    print(cat1.get_variables('feet'))
    
if __name__ == "__main__": main()
