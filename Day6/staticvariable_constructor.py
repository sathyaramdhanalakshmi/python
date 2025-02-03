class Car1:
    brandc = "Generic Brand"  # Static variable

    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def model_name(self):
        return self.name

    def car_mileage(self):
        return self.mileage

class Car2(Car1):  
    brandd = "Maruti"  # Static variable

    def __init__(self, name, mileage, color):
        super().__init__(name, mileage)  
        self.color = color

    def model(self):
        print("Maruti")

# Creating an instance of Car1
car = Car1("Maruti", '500')

brandc = "Toyota"  # Updates static variable

# Printing results
print("Car Name:", car.model_name())  
print("Mileage:", car.car_mileage())  
print("Car1 Brand:", car.brandc)  # Accessing updated static variable        