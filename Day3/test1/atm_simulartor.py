def check_balance(balance):
    enteredpassword=int(input("enter password: "))
    savedpassword=1234
    if enteredpassword==savedpassword:
        print(f"current balance is {balance}")
    else:
        print("incorrect password, try again")
        check_balance(balance)
        
def deposit_money(balance):
    amount=int(input("enter amount: "))
    balance+=amount
    print(f"money deposited successfully,current balance is {balance}")
    print("thank you for using atm")
    
def withdraw_money(balance):
    withdrawamount=int(input("enter amount to withdraw: "))
    if withdrawamount<=0:
        print("invalid, enter a positive integer")
        withdraw_money(balance)
    elif withdrawamount>balance:
        print("insufficient balance ,enter a smaller amount")
        withdraw_money(balance)
    elif withdrawamount<=balance:
        balance-=withdrawamount
        print(f"amount successfully withdrawn,current balance: {balance}")
        print("thank you for using atm")
        
def main():
    balance=10000
    print("1.check balance")
    print("2.deposit money")
    print("3.withdraw money")
    print("4.exit")
    
    inp=int(input("select a option: "))
    
    if inp==1:
        check_balance(balance)
    elif inp==2:
        deposit_money(balance)
    elif inp==3:
        withdraw_money(balance)
    elif inp==4:
        print("thank you for using atm")
    else:
        print("invalid,select correct option from 1 to 4")
        main()
main()