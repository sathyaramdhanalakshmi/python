class BankAccount:
    def __init__(self, balance = 0):
        self.balance= balance
        
    def deposite(self, amount):
        if amount > 0:
            self.balance+=amount
            print(f"The deposited amount is : {self.balance}")
        else:
            print("invalid amount ")
            
    def withdraw(self, amount):
        if amount > 0 :
            if self.balance >= amount:
                self.balance-=amount
                print(f"The withdrawn amount is:{self.balance}")
            else:
                print("insufficent balance")
        else:     
            print(f"invalid amount")
        
obj=BankAccount()
obj.deposite(5000)
obj.withdraw(1500)
