class Electronics:
    
    def __init__(self, name , price):
        self.name = name
        self.price = price
        
    def display(self):
        print (f"Brand: {self.name}\n price: {self.price}")
        
class MobileDevice(Electronics):
    
    def __init__(self, name, price, batterry):
        super().__init__(name, price)
        self.battery = batterry
        
    def display(self):
        super().display()
        print(f"battery : {self.battery}")
        
class Smartphone(MobileDevice):
    
    def __init__(self, name, price, battery, camera_quality):
        super().__init__(name, price, battery)
        self.camera_quality= camera_quality
        
    def display(self):
        super().display()
        print(f"camera:{self.camera_quality}")
        
obj= Smartphone("Apple", 115000, 128 , 150)
obj.display()
        
        
        
        
    