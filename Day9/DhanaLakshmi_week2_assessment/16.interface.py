import math
from abc import ABC, abstractmethod

class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    
class Rectangle(IShape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth  
    
    def calculate_area(self):
        return self.length * self.breadth  
    
class Circle(IShape):
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        return math.pi * (self.radius ** 2) 

rectangle = Rectangle(5, 3)
circle = Circle(4)

# Calculate and display areas
print(f"Area of Rectangle: {rectangle.calculate_area()}")
print(f"Area of Circle: {circle.calculate_area()}")