def list():
    L1 = []
    sum=0
    for _ in range(5):  # Loop runs 5 times
        value = int(input("Enter a value: "))
        sum+=value
        L1.append(value)
        
    return L1,sum

def main():
    L1,sum=list()
    print("sum of the elements in list is : ",sum)

main()