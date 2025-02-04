import csv
from abc import ABC, abstractmethod
from typing import List

# Step 1: Define Employee interface using Abstract Base Class (ABC)
class Employee(ABC):
    @abstractmethod
    def work(self) -> str:
        pass
    
    @abstractmethod
    def get_salary(self) -> float:
        pass
    
    @abstractmethod
    def promote(self) -> None:
        pass
    
    @abstractmethod
    def increment_salary(self) -> None:
        pass


# Step 2: Create concrete classes for different types of employees

class Manager(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        self.role = "Manager"

    def work(self) -> str:
        return f"{self.name} is managing the team"

    def get_salary(self) -> float:
        return self.salary
    
    def promote(self) -> None:
        self.role = "Senior Manager"
        print(f"{self.name} has been promoted to {self.role}")

    def increment_salary(self) -> None:
        self.salary += 10000
        print(f"The incremented salary for {self.name}: {self.salary}")


class Developer(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        self.role = "Developer"

    def work(self) -> str:
        return f"{self.name} is writing code."

    def get_salary(self) -> float:
        return self.salary
    
    def promote(self) -> None:
        self.role = "Senior Developer"
        print(f"{self.name} has been promoted to {self.role}")

    def increment_salary(self) -> None:
        self.salary += 60000
        print(f"The incremented salary for {self.name}: {self.salary}")


class Intern(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        self.role = "Intern"

    def work(self) -> str:
        return f"{self.name} is learning and assisting"

    def get_salary(self) -> float:
        return self.salary
    
    def promote(self) -> None:
        self.role = "Junior Developer"
        print(f"{self.name} has been promoted to {self.role}")

    def increment_salary(self) -> None:
        self.salary += 10000
        print(f"The incremented salary for {self.name}: {self.salary}")


# Step 3: Define Department class that manages Employees

class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees: List[Employee] = []

    def hire(self, employee: Employee) -> None:
        self.employees.append(employee)
        print(f"{employee.name} has been hired as a {employee.role}")

    def fire(self, employee: Employee) -> None:
        self.employees.remove(employee)
        print(f"{employee.name} has been fired")

    def get_total_salary(self) -> float:
        return sum(employee.get_salary() for employee in self.employees)

    def promote(self, employee: Employee) -> None:
        employee.promote()

    def increment_salary(self, employee: Employee) -> None:
        employee.increment_salary()

    def show_employee_details(self) -> None:
        print(f"Employees in {self.name} Department:")
        for employee in self.employees:
            print(f"- {employee.name}, Role: {employee.role}, Salary: {employee.get_salary()}, Work: {employee.work()}")

    # Method to write employee details to a CSV file
    def write_to_csv(self, filename: str) -> None:
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Role', 'Salary', 'Work']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for employee in self.employees:
                writer.writerow({
                    'Name': employee.name,
                    'Role': employee.role,
                    'Salary': employee.get_salary(),
                    'Work': employee.work()
                })
        print(f"Employee details have been written to {filename}")


class Security(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        self.role = "Security Staff"

    def work(self) -> str:
        return f"{self.name} is securing the assets"

    def get_salary(self) -> float:
        return self.salary
    
    def promote(self) -> None:
        self.role = "Head of Security"
        print(f"{self.name} has been promoted to {self.role}")

    def increment_salary(self) -> None:
        self.salary += 5000
        print(f"The incremented salary for {self.name}: {self.salary}")


# Step 4: Create department and add employees

# Create employees
manager = Manager("Alice", 8000)
developer = Developer("Bob", 60000)
intern = Intern("Charlie", 20000)
security_staff = Security("Ram", 5000)

# Create a department and hire employees
it_department = Department("IT")
it_department.hire(manager)
it_department.hire(developer)
it_department.hire(intern)
it_department.hire(security_staff)

# Show employee details
it_department.show_employee_details()

# Promote an employee
it_department.promote(developer)
it_department.promote(intern)
it_department.promote(security_staff)
it_department.promote(manager)

# Increment salary for an intern
it_department.increment_salary(intern)
it_department.increment_salary(developer)
it_department.increment_salary(security_staff)
it_department.increment_salary(manager)

# Write employee details to CSV
it_department.write_to_csv('employees.csv')

# Total salary in the department
total_salary = it_department.get_total_salary()
print(f"Total salary expense for {it_department.name} department: ${total_salary}")