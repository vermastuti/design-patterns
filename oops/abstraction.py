# example of abstraction
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass    

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
if __name__ == "__main__":

    dog = Dog()
    cat = Cat()
    
    print(dog.make_sound())  # Output: Woof!
    print(cat.make_sound())  # Output: Meow!"""
# This code demonstrates the concept of abstraction in object-oriented programming using Python's `abc` module.

"""
    # This code demonstrates the concept of abstraction in object-oriented programming using Python's `abc` module.
    # The `Animal` class is an abstract base class with an abstract method `make_sound`.
    # The `Dog` and `Cat` classes inherit from `Animal` and provide concrete implementations of the `make_sound` method.
    # When we create instances of `Dog` and `Cat` and call their `make_sound` methods, we get the respective sounds of the animals.
    # This shows how abstraction allows us to define a common interface for different subclasses while hiding the implementation details.
"""