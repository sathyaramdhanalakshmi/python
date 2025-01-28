import math
def prime_num(n):
    if n<=1:
        return 0
    if n==2:
        return 1
    if n%2==0:
        return 0
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            return 0
    return 1
def get_input():
    n=int(input("enter n value: "))
    return n

def main():
    n=get_input()
    ans=prime_num(n)
    if ans==1:
        print(f"{n} is prime")
    else:
        print(f"{n} is not a prime")
    
main()