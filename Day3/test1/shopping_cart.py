def display():
    print("\nselect a option")
    print("1.Add item")
    print("2.View cart")
    print("3.Calculate total price")
    print("4.Exit")

def add_item(cart):
    name = input("Enter the item name: ")
    price = float(input(f"Enter the price of {name}: "))
    cart[name] = price
    print(f"{name} added to the cart.")

def view_cart(cart):
    if not cart:
        print("\nYour cart is empty.\n")
    else:
        print("\nItems in your cart:")
        for item, price in cart.items():
            print(f"{item}:{price:.2f}")

def calculate_total(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        total = sum(cart.values())
        print(f"\nTotal price of items in the cart: {total:.2f}\n")

def main():
    cart = {}  
    while True:
        display()
        choice = input("Enter your choice : ")
        if choice == '1':
            add_item(cart)
        elif choice == '2':
            view_cart(cart)
        elif choice == '3':
            calculate_total(cart)
        elif choice == '4':
            print("Thank you for shopping")
            break
        else:
            print("Invalid choice,select correct option from 1 to 4")
            
main()