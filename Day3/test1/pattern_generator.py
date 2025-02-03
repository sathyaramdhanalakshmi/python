def print_reverse_pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)
def print_pattern(n):
    for i in range(1, n + 1):
        print("*" * i)

def main():
    
    n = int(input("Enter n value: "))
    if n <= 0:
        print("Please enter a positive integer.")
        return
    reverse_option = input("Do you want the pattern in reverse? enter yes/YES or no : ")
    reverse = "yes" or "YES"
    if reverse_option ==reverse:
        print_reverse_pattern(n)
    else:
        print_pattern(n)
        
main()