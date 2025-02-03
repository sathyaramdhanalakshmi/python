class Gender:
    def display_gender(self):
        pass

class Man(Gender):
    def __init__(self, name):
        self.name = name  

    def get_name(self):
        return self.name
    
    def display_gender(self):
        return "Male"
    
class Woman(Gender):
    def __init__(self, name):
        self.name = name  

    def get_name(self):
        return self.name
        
    def display_gender(self):
        return "Female"

obj1 = Man("Ram")
obj2 = Woman("Seetha")

print(f"{obj1.get_name()} is {obj1.display_gender()}")  
print(f"{obj2.get_name()} is {obj2.display_gender()}")  
