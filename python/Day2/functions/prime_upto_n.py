def prime(n):
    if n<=1:
        return False
    
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def get_input():
    n=int(input("enter n val: "))
    return n

def main():
    n=get_input()
    print(f"prime numbers upto {n} are: ")
    for i in range(1,n+1):
        if prime(i):
            print(i,end=" ") 
                
main()
