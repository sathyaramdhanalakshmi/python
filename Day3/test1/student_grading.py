def display(totalmarks,percentage,grade):
    print(f"total marks is: {totalmarks} , percentage is: {percentage} , grade is {grade}")
    
def student_names():
    name=input("enter student name:")
    s1=input("enter subject1 marks: ")
    s2=input("enter subject2 marks: ")
    s3=input("enter subject3 marks: ")
    s4=input("enter subject4 marks: ")
    s5=input("enter subject5 marks: ")
    return (name,s1,s2,s3,s4,s5)

def total_marks(s1,s2,s3,s4,s5):
    totalmarks=float(s1)+float(s2)+float(s3)+float(s4)+float(s5)
    return totalmarks

def find_percentage(totalmarks):
    perc=(totalmarks/500)*100
    return perc

def assign_grade(perc):
    if perc>=80 and perc<=100:
        grade="A"
    elif perc>=60 and perc<80:
        grade="B"
    elif perc>=40 and perc<60:
        grade="C"
    elif perc>=0 and perc<40:
        grade="FAIL"
    return grade

def main():
    name,s1,s2,s3,s4,s5=student_names()
    totalmarks=total_marks(s1,s2,s3,s4,s5)
    percentage=find_percentage(totalmarks)
    grade=assign_grade(percentage)
    display(totalmarks,percentage,grade)
    
main()
    