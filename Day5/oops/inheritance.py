#self is a keyword to use inside class
#self is intermediator between caller and class

class Parent:
    def __init__(self):           #parent constructor
        self.parentname="sahithi"
        
    def display_parent(self):
        print("this is parent class")

class Child(Parent):
    def __init__(self):          #child constructor
        super().__init__()
        self.childname="kid"
        
    def display_child(self):
        print("this is child class")

child=Child()
child.display_child()
child.display_parent()
print(child.parentname)
print(child.childname)

p=Parent()
