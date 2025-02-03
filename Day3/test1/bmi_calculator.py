def bmi_calculator(weight,height):
    bmi=weight/(height**2)
    return bmi

def bmi_category(bmi):
    if bmi<=18.5:
        print("underweight")
    elif bmi>18.5 and bmi<=24.9:
        print("normal weight")
    elif bmi>24.9 and bmi<=29.9:
        print("overweight")
    else:
        print("obese")

def main():
    weight=float(input("enter weight in kgs: "))
    height=float(input("enter height in meters: "))
    bmi=bmi_calculator(weight,height)
    print(bmi)
    bmi_category(bmi)
    
main()
    