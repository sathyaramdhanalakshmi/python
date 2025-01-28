# constructor is a special method that is automatically called when an object of a class is created

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def display_info(self):
        print(f"the car is a {self.brand} {self.model}")
        
car1=Car("Toyota","BMW")
car2=Car("rr","maruthi")
car1.display_info()
car2.display_info()