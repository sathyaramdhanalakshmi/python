def separate_odd_even(numbers):
    even = [i for i in numbers if i % 2 == 0]
    odd = [i for i in numbers if i % 2 != 0]
    return even,odd

def main():
    listofnumbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    even,odd = separate_odd_even(listofnumbers)
    print(f"Even numbers are: {even}")
    print(f"Odd numbers are: {odd}")
    

    
main()