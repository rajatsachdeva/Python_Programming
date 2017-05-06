#!/usr/bin/python3

# Classes in python
# Inheritance
# When one class inherits the properties of another class
# The class that is being inherited from is often called a base class or a parent class

# Parent Class
class Animal:
    def talk(self): print("I have something to say!")
    def walk(self): print("Hey!, I'm walking here !")
    def clothes(self): print("I have nice clothes")
    
# Inherits the Animal Class
class Duck(Animal):
    def quack(self):
        print('Quaaack!')

    # Over-riding the walk function 
    # When the child class overrides the base class function 
    # with it's own functionality
    def walk(self):
        # Super method allows the child class to call the parent's defined method
        # from the overriden method
        super().walk()
        print('Walks like a duck.')

# Define a Dog class
class Dog(Animal):
    def clothes(self):
        super().clothes()
        print("I Have brown and white fur")
    
def main():
    # create an Instance/object of Duck class
    donald = Duck()
    print(donald)
    donald.quack()
    donald.walk()
    donald.talk()
    donald.clothes()
    print("\nDog")
    fido = Dog()
    fido.walk()
    fido.talk()
    fido.clothes()

if __name__ == "__main__": main()
