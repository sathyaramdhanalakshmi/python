def array():
    arr=[]
    for _ in range(10):
        val=int(input("enter a value: "))
        arr.append(val)
    return arr
def main():
    print(array())
main()