class Car1:

    def __init__(self, name=None, mileage=None):
        if name:
            print(f"car name: {name}")
        if mileage:
            print(f"car mileage: {mileage}")
        
obj = Car1(mileage=25)  # It calls the constructor with mileage.

class Example:
    def __init__(self, *args):
        if len(args) == 1:
            print(f"hello {args[0]}")
        elif len(args) == 2:
            print(f"Hello {args[0]}, you are {args[1]} years old")
            
obj1 = Example("Alice",30)

class Example2:
    def __init__(self, studentName, **kwargs):
        self.studentName = studentName
        if "name" in kwargs and "age" in kwargs:
            print(f"hello {kwargs['name']}, you are {kwargs['age']} years old")
        elif "name" in kwargs:
            print(f"hello {kwargs['name']}")
        
        # Fixed typo here
        self.inputname = kwargs['name']  
        
obj1 = Example2(studentName="Student", name="Dhana" , age=20)
print("elements in kwargs is", obj1.inputname)
