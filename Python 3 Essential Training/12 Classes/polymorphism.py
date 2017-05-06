#!/usr/bin/python3

# Classes in python

# Polymorphism
# It's the practice of using one particular class as if it were 
# object of another class

# Python is what is called as loosely typed/duck typing
# so a strong advantage of this loosely typed is that polymorphism is natural

# define a class
class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
        
    def Bark(self):
        print("The duck cannot bark")
    
    def fur(self):
        print("The duck has feathers")
        
class Dog:
    def Bark(self):
        print("Woof !")
    
    def fur(self):
        print("the dog has brown and white fur")

    def quack(self):
        print('Dog cannot Quack')

    def walk(self):
        print('Walks like a Dog.')
                
def main():
    # create an Instance/object of Duck class
    donald = Duck()
    fido = Dog()
    
    for obj in (donald, fido):
        obj.Bark()
        obj.fur()
        obj.quack()
        obj.walk()
        
    print()
    in_the_forest(donald)
    in_the_forest(fido)
    
def in_the_forest(dog):
    dog.Bark()
    dog.fur()
    
def in_the_pond(duck):
    duck.quack()
    duck.walk()
    
if __name__ == "__main__": main()
