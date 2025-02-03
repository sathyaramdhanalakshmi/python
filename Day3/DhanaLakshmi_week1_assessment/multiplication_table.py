def take_input():
    n=input("enter a number: ")
    return n

def generate_and_print(n):
    print(f"{n} * 1 ={int(n)}")
    print(f"{n} * 2 ={int(n)*2}")
    print(f"{n} * 3 ={int(n)*3}")
    print(f"{n} * 4 ={int(n)*4}")
    print(f"{n} * 5 ={int(n)*5}")
    print(f"{n} * 6 ={int(n)*6}")
    print(f"{n} * 7 ={int(n)*7}")
    print(f"{n} * 8 ={int(n)*8}")
    print(f"{n} * 9 ={int(n)*9}")
    print(f"{n} * 10 ={int(n)*10}")
    
def main():
    n=take_input()
    generate_and_print(n)
    
main()