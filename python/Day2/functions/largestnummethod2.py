def display(value,ans):
    print(f"the largest number among 4 numbers is {ans}:{value}")
    
def get_input_compute():

    a=input("enter a value: ")
    b=input("enter b value: ")
    c=input("enter c value: ")
    d=input("enter d value: ")
    
    max=a
    if b>max:
        max=b
        k="b"
    
    if c>max:
        max=c
        k="c"
    
    if d>max:
        max=d
        k="d"
        
    return (max,k)
        
def main():
    max,k=get_input_compute()
    display(max,k)
    
main()  