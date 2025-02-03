def leap_year_checker(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    return False

def main():
    year=int(input("enter a year: "))
    if year<=0:
        year=print("enter a valid year:")
    if leap_year_checker(year):
        print(f"{year} is leap year")
    else:
        print(f"{year} is not a leap year")

main()