import threading
import time

print("main thread execution is started")

def print_odd(start, end):
    print("sub task to find odd num is started")
    for i in range(start, end+1):
        if i % 2 != 0:
            print(f"Odd: {i}")
            time.sleep(2)
    print("sub task odd is completed")

def print_even(start, end):
    print("sub task to find even num is started")
    for i in range(start, end+1):
        if i % 2 == 0:
            print(f"Even: {i}")
            time.sleep(2)
    print("sub task even is completed")


start = int(input("enter a starting num: "))
end = int(input("enter the ending num: "))

odd = threading.Thread(target=print_odd, args=(start, end))
even = threading.Thread(target=print_even, args=(start, end))
odd.start()
even.start()
odd.join()
even.join()
print("main thread execution completed ")
