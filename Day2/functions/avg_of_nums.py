def display(res):
    print(f"the average of these numbers are : {res}")
    
def get_input():
    a=input("a: ")
    b=input("b: ")
    c=input("c: ")
    d=input("d: ")
    
    return (a,b,c,d)

def get_sum(a,b,c,d):
    sum=(int(a)+int(b)+int(c)+int(d))

    return sum

def compute_average(val):
    avg=val/4
    
    return avg
    
def main():
    (a,b,c,d)=get_input() #taking input
    sum=get_sum(a,b,c,d)  #calling sum function
    average=compute_average(sum)  #calling avg function by giving sum as input
    display(average) #display the ans by calling display function
    
main()
    