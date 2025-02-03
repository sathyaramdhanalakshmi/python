#An interface is a blueprint that defines a set of methods that a class must implement.
# It ensures that different classes follow a common structure without providing actual implementations.
#ABC is abstract base class used to define interface from abc module

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod      #it ensures that subclasses must implement the methods
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("bark")

class Cat(Animal):
    def make_sound(self):
        print("meow")

obj1 = Dog()
obj2 = Cat()
obj1.make_sound()
obj2.make_sound()