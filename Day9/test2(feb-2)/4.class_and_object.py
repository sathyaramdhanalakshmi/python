class Student:
    def __init__(self, name, rollno):
        self.name=name
        self.rollno=rollno
        
    def student_details(self):
        print(f"The name of the student is: {self.name}")
        print(f"The rool number of the student is:{self.rollno}")
    
obj=Student("dhana","573")
obj.student_details()
