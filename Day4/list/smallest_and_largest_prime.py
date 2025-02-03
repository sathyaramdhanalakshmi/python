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
    L=[]
    print(f"prime numbers from {start} to {endd} are: ")
    for i in range(start,endd+1):
        if prime(i):
            print(i,end=" ") 
            L.append(i)
    if L:  
        print("\nSmallest prime:", L[0], "Largest prime:", L[-1])  # Use L[-1] for the last element
    else:
        print("\nNo prime numbers found in the given range.")
                
main()
