def display(amount):
    print(f"each member have to pay the amount of {amount} rupees")
    
def take_input():
    bill=float(input("enter bill: "))
    people=float(input("enter no of people:"))
    tip=float(input("enter tip percentage:"))
    return (bill,people,tip)

def split_bill(bill,people,tip):
    totalwithtip=bill+(bill*tip/100)
    eachperson=totalwithtip/people
    return eachperson
    
def main():
    bill,people,tip=take_input()
    eachhavetopay=split_bill(bill,people,tip)
    display(eachhavetopay)
main()