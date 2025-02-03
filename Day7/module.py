#******from cal import add as s*****
#domain driven development

import customermodule,orders_module,order_itemsmodule
print("***************************************************************")

customer1 = customermodule.Customer(1, "John", "Doe", "123-456-7890", "john.doe@example.com", "123 Main St", "New York", "NY", "10001")
customer1.display_info()
print("***************************************************************")

order1 = orders_module.Order(101, 1, "Shipped", "2023-10-01", "2023-10-05", "2023-10-03", 1, 1)
order1.display_info()
print("***************************************************************")

order_item1 = order_itemsmodule.OrderItems(101, 1, 1001, 1, 499.99, 0.1)
order_item1.display_info()
print("***************************************************************")