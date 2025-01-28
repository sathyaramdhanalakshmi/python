# 

class School:
    def __init__(self, schoolname, student_id, std_name, age, passout):
        self.schoolname = schoolname
        self.student_id = student_id
        self.std_name = std_name
        self.age = age
        self.passout = passout
    
    def display_school(self):
        print(f"School Name: {self.schoolname}")
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.std_name}")
        print(f"Age: {self.age}")
        print(f"Passout Year: {self.passout}")

class College(School):
    def __init__(self, schoolname, student_id, std_name, age, passout, college_type):
        super().__init__(schoolname, student_id, std_name, age, passout)
        self.college_type = college_type
    
    def display_PG_college(self):
        if self.college_type == "PG":
            print("This school is now a PG college.")
    
    def display_UG_college(self):
        if self.college_type == "UG":
            print("This school is now a UG college.")

# Example usage:
college = College("TSRS", "1001", "Dhanalakshmi", 20, 2023, "PG")
college.display_school()
college.display_PG_college()
college.display_UG_college()
print(f"College Type: {college.college_type}")
