#module is a file containing python definitions ans statements

class Customer:
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

    def display_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Phone: {self.phone}, Email: {self.email}")
        print(f"Address: {self.street}, {self.city}, {self.state}, {self.zip_code}")
        

