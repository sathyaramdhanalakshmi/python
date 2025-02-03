#adding employee details to the list

class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.salary=salary
        self.id=id
        
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def get_salary(self):
        return self.salary
    
List=[]
emp=Employee("Alice",23,5000)
List.append(emp.get_name())
List.append(emp.get_id())
List.append(emp.get_salary())
print("the List with name ,id and salary",List)

#(*args)=by adding star we can give any number of parameter
#(**kwargs) named aregument comes with 2 stars,when we give input from outside constructor it will not take,it will work with in that constructor 