class Customers:
    def __init__(self, customer_id, first_name, last_name, phone, email, street, city, state, zip_code):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def get_details(self):
        return (
            self.customer_id, self.first_name, self.last_name, 
            self.phone, self.email, self.street, self.city, 
            self.state, self.zip_code
        )

class Orders(Customers):
    def __init__(self, customer_id, first_name, last_name, phone, email, street, city, state, zip_code,
                 order_id, order_status, order_date, required_date, shipped_date, store_id, staff_id):
        super().__init__(customer_id, first_name, last_name, phone, email, street, city, state, zip_code)
        self.order_id = order_id
        self.order_status = order_status
        self.order_date = order_date
        self.required_date = required_date
        self.shipped_date = shipped_date
        self.store_id = store_id
        self.staff_id = staff_id
    
    def get_details(self):  # Polymorphism
        customer_details = super().get_details()
        
        return customer_details + (self.order_id, self.order_status, self.order_date, self.required_date, self.shipped_date, self.store_id, self.staff_id)
        

class OrderItems(Orders):
    def __init__(self, customer_id, first_name, last_name, phone, email, street, city, state, zip_code,
                 order_id, order_status, order_date, required_date, shipped_date, store_id, staff_id,
                 item_id, product_id, quantity, list_price, discount):
        super().__init__(customer_id, first_name, last_name, phone, email, street, city, state, zip_code,
                         order_id, order_status, order_date, required_date, shipped_date, store_id, staff_id)
        self.item_id = item_id
        self.product_id = product_id
        self.quantity = quantity
        self.list_price = list_price
        self.discount=discount
    
    def get_details(self):  # Polymorphism
        order_details = super().get_details()
        return order_details + (
            self.item_id, self.product_id, self.quantity, self.list_price, self.discount
        )


# Creating an instance of OrderItems
order_item = OrderItems(
    "573", "Dhana", "Lakshmi", 9874563210, "sdl@gmail.com", "KP", "Hyd", "TS", 502220,
    "ORD001", "Shipped", "2024-01-10", "2024-01-15", "2024-01-12", "S001", "STF123",
    "ITM001", "PRD567", 2, 1500.00, 10.0
)

print(order_item.get_details())

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Customer Class
class Customer:
    def _init_(self, customer_id, first_name, last_name, phone, email, street, city, state, zip_code):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def display_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Phone: {self.phone}, Email: {self.email}")
        print(f"Address: {self.street}, {self.city}, {self.state}, {self.zip_code}")


# Order Class
class Order:
    def _init_(self, order_id, customer_id, order_status, order_date, required_date, shipped_date, store_id, staff_id):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_status = order_status
        self.order_date = order_date
        self.required_date = required_date
        self.shipped_date = shipped_date
        self.store_id = store_id
        self.staff_id = staff_id

    def display_info(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Status: {self.order_status}")
        print(f"Order Date: {self.order_date}")
        print(f"Required Date: {self.required_date}")
        print(f"Shipped Date: {self.shipped_date}")
        print(f"Store ID: {self.store_id}, Staff ID: {self.staff_id}")


# OrderItems Class
class OrderItems:
    def _init_(self, order_id, item_id, product_id, quantity, list_price, discount):
        self.order_id = order_id
        self.item_id = item_id
        self.product_id = product_id
        self.quantity = quantity
        self.list_price = list_price
        self.discount = discount

    def display_info(self):
        print(f"Order ID: {self.order_id}, Item ID: {self.item_id}")
        print(f"Product ID: {self.product_id}, Quantity: {self.quantity}")
        print(f"List Price: {self.list_price}, Discount: {self.discount}")


# Create a customer
customer1 = Customer(1, "John", "Doe", "123-456-7890", "john.doe@example.com", "123 Main St", "New York", "NY", "10001")
customer1.display_info()

# Create an order
order1 = Order(101, 1, "Shipped", "2023-10-01", "2023-10-05", "2023-10-03", 1, 1)
order1.display_info()

# Create an order item
order_item1 = OrderItems(101, 1, 1001, 1, 499.99, 0.1)
order_item1.display_info()