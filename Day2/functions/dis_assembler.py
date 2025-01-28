import dis

def display(val):
    print(f"the answer is {val}")
    
def get_input():
    a=input("a value: ")
    b=input("b value: ")
    return (a,b)

def multiply(a,b):
    res=int(a)*int(b)
    return res

def main():
    a,b=get_input()
    ans=multiply(a,b)
    display(ans)
    dis.dis(get_input)
    
main()