from abc import ABC, abstractmethod

class Father(ABC):
    def __init__(self, father_pan):
        self.father_pan = father_pan

    @abstractmethod             
    def display(self):
        pass

    def show(self):  
        print("Father PAN card with name:", self.father_pan)                 

class Child(Father):
    def __init__(self, father_pan, child_pan):
        super().__init__(father_pan)
        self.child_pan = child_pan

    def display(self):
        print(f"Child PAN card with name: {self.child_pan}, inherited from parent PAN card with father name: {self.father_pan}")

father_pan = input("Enter Father's PAN card name: ")
child_pan = input("Enter Child's PAN card name: ")

obj = Child(father_pan, child_pan)
obj.show()
obj.display()
