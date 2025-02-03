from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def max_speed(self):
        pass

class Car(Vehicle):
    def max_speed(self):
        return 200

class Bike(Vehicle):
    def max_speed(self):
        return 150

car = Car("Tesla")
bike = Bike("Yamaha")

print(f"{car.brand} Max Speed: {car.max_speed()} km/h")  
print(f"{bike.brand} Max Speed: {bike.max_speed()} km/h") 