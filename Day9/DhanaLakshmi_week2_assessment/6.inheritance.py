class Vehicle:
    def get_vehicle(self):
        print("this is vehicle class")
        
class car(Vehicle):
    def get_car(self):
        print("this is car class")
        
class Bike(Vehicle):
    def get_bike(self):
        print("this is bike class")
        
class ElectricCar(car):
    def get_ElectricCar(self):
        print("this is ElectricCar class")
        
obj1= ElectricCar()
obj1.get_ElectricCar()
obj1.get_car()
obj1.get_vehicle()
obj2= Bike()
obj2.get_bike()

