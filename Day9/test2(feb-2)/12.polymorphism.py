class Payment:
    def process_payment(self, amount):
        print(f"Processing a payment of {amount}")

class CreditCard_Payment(Payment):
    def process_payment(self, amount):
        print(f"Processing a credit card payment of {amount}")


class PayPal_Payment(Payment):
    def process_payment(self, amount):
        print(f"Processing a PayPal payment of {amount}")

class Bitcoin_Payment(Payment):
    def process_payment(self, amount):
        print(f"Processing a Bitcoin payment of {amount}")


obj1 = CreditCard_Payment()
obj1.process_payment(500) 

obj2 = PayPal_Payment()
obj2.process_payment(100)   

obj3 = Bitcoin_Payment()
obj3.process_payment(300)  
