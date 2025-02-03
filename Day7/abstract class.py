#abstract class is a method whose action is defined in the 
#concrete class is defined in th abstract class it self
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

d = Dog()
d.make_sound()  # Output: Bark!

c = Cat()
c.make_sound()  # Output: Meow!
