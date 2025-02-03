class Employee:
    
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary
        
    def set_salary(self,salary):
        self._salary=salary
        
    def get_salary(self):
        return self._salary
    
    def calculate_net_salary(self, allowance, deduction):
        net_salary = self._salary + allowance - deduction
        return net_salary
    
emp=Employee("Alice",5000)
print("salary before update",emp.get_salary())

emp_updated_salary=int(input("enter salary to update: "))
emp.set_salary(emp_updated_salary)
print("salary after update",emp.get_salary())

allowance = int(input("Enter allowance: "))
deduction = int(input("Enter deduction: "))
net_salary = emp.calculate_net_salary(allowance,deduction)
print(f"Net salary after allowance and deduction: {net_salary}")