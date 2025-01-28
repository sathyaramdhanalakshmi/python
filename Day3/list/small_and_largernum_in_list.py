def take_input():
    L1=[]
    n=int(input("enter size of list: "))
    for i in range(n):
        value=int(input("enter elements: "))
        L1.append(value)
    return L1

def find_smallest_largest(L1):
    smallest=biggest=L1[0] 
    for i in L1:
        if i<smallest:
            smallest=i
        if i>biggest:
            biggest=i
    return smallest,biggest

def dispaly(smallest, largest):
    print("smallest element: ",smallest," and largest element: ",largest)
    
def main():
    L1=take_input()
    smallest, largest=find_smallest_largest(L1)
    dispaly(smallest, largest)
main()










#another way of taking list L1=list(map(int,input(f"enter {n} integers: ).split()))
#smallest=sorted(L1)[0]  #largest=sorted(L1)[-1]