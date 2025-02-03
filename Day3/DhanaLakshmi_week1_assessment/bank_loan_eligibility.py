def take_input():
    salary=int(input("enter salary: "))
    age=int(input("enter age: "))
    creditscore=int(input("enter credit score: "))
    return (salary,age,creditscore)
def loan_status(salary,age,creditscore):
    if salary<50000:
        if age>=21 and age<=60:
            if creditscore>700:
                print(f"loan is approved")
            else:
                print(f"your credit score is less, loan is rejected")
        else:
            print(f"your age in not satisfied, loan is rejected")
    else:
        print(f"your salary is greater than the limit, loan is rejected")
def main():
    salary,age,creditscore=take_input()
    loan_status(salary,age,creditscore)
    
main()
                
        