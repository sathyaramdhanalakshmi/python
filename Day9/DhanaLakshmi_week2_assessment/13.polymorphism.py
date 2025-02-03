class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height  

square = Square(4)
print(f"Square Area: {square.area()}") 

triangle = Triangle(5, 3)
print(f"Triangle Area: {triangle.area()}")  
