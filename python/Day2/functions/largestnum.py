def display(ans):
    print(f"the largest number among 3 numbers is {ans}")
    
def get_input():
    a=input("enter a value: ")
    b=input("enter b value: ")
    c=input("enter c value: ")
    
    return (a,b,c)
        

def get_largest_num(a,b,c):
    if a>b and a>c :
        largest=a
    elif b>a and b>c :
        largest=b
    else:
        largest=c
        
    return largest

def main():
    a,b,c=get_input()
    averagenum=get_largest_num(a,b,c)
    display(averagenum)
    
main()  