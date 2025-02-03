class Car():
    def move(self):
        print(f"car can move forward and backward")
        
class Airplane():
    def move(self):
        print(f"moves on the sky")
        
class FlyingCar(Car,Airplane):
    def move(self):
        print(f"moves on ground and sky")
        
obj1=FlyingCar()
obj1.move()

obj2=Airplane()
obj2.move()

obj3=Car()
obj3.move()