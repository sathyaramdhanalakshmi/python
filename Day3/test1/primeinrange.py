def prime(n):
    if n<=1:
        return False
    
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def get_input():
    start=int(input("enter start value: "))
    end=int(input("enter end value: "))
    return (start,end)

def main():
    start,endd=get_input()
    print(f"prime numbers from {start} to {endd} are: ")
    for i in range(start,endd+1):
        if prime(i):
            print(i,end=" ") 
                
main()
