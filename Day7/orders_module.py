class Order:
    def __init__(self, order_id, customer_id, order_status, order_date, required_date, shipped_date, store_id, staff_id):
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
