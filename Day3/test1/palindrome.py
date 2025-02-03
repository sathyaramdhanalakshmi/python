def palindrome(value):
    value=str(value)
    return value==value[::-1]
def take_input():
    inp=input("enter a string or number :")
    return inp
def main():
    value=take_input()
    if palindrome(value):
        print(f"{value} is palindrome")
    else:
        print(f"{value} is not palindrome")
    
main()