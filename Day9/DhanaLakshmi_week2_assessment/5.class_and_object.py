class product:
    
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        
    def check_availability(self, quantity):

        if quantity <= self.stock :
            print(f" {quantity} , {self.name}'s are available")
        else:
            print(f"{quantity} request product {self.name} are not available")
    
    
obj=product("tv",100000, 12)
print(obj.check_availability(10))