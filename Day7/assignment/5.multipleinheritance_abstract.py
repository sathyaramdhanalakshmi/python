from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_name(self):
        pass

class Employee(ABC):
    @abstractmethod
    def get_salary(self):
        pass

class Manager(Person, Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

m = Manager("Alice", 90000)
print(f"Manager Name: {m.get_name()}")  # Output: Alice
print(f"Manager Salary: {m.get_salary()}")  # Output: 90000
