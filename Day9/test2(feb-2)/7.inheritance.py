class person():
    def __init__(self, name, qualification):
        self.name = name
        self.qualification = qualification
        
    def details(self):
        print(f"{self.name} : {self.qualification}")
        
class Employee(person):
    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department
        
    def details(self):
        print(f"nmae: {self.name} , id: {self.id} , department: {self.department}")
        
class Manager(person):
    def __init__(self, name, id, department):
        self.name= name
        self.id= id
        self.department= department
        
    def details(self):
        print(f"name: {self.name} , name: {self.id} , name: {self.department}")
        
    def approve_leave(self):
        print(f"Manager {self.name} has approved the leave")
        
obj =Manager("Alice", 573 , "manager")
obj.details()
obj.approve_leave()