def find_factorial(n):
    
    ans=1
    for i in range(2,n+1):
        ans=ans*i
    return ans
    
def main():
    num=int(input("enter a number:"))
    ans=find_factorial(num)
    print(ans)
main()