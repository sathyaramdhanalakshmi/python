from abc import ABC, abstractmethod

class Father(ABC):
    # Abstract method without body
    @abstractmethod             
    def display(self):
        pass

    # Concrete method with body
    def show(self):                   
        print("Concrete method")

class Son(Father):
    def display(self):
        print("son is implementing the abstract method")

class Daughter(Father):
    def display(self):
        print("Daughter is implementing the abstract method")


obj1 = Son()
obj1.display()
obj1.show() 

obj2=Daughter()
obj2.display()# Output: Implementation of abstract method in Child 
obj2.show()# Output: Concrete method
