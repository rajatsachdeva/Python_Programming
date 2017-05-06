#!/usr/bin/python3

# Decorators in Python
# Decorators are special functions that return other functions and 
# They are used to modify the way the function works

class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)
   
    @property
    def color(self):
        return self.properties.get('color', None)

    @color.setter
    def color(self, c):
        self.properties['color'] = c
        
    @color.deleter
    def color(self):
        del self.properties['color']
        
def main():
    donald = Duck()
    print(donald.get_property('color'))
    donald.color = 'blue'
    print(donald.color)

if __name__ == "__main__": main()
