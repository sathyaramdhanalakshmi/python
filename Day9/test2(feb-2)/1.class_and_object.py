class Employee:
    def __init__(self, name , id , dept):
        self.name=name
        self.id=id
        self.dept=dept
        
emp=Employee("dhana" , 73 , "cse")
print(f"name:{emp.name}, id:{emp.id}, department:{emp.dept}")
