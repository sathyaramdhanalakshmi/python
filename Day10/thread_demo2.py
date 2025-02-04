import threading
import time

def sub_task1():
    while True:
        print("sub task1 is running...")
        time.sleep(1)
        break

def  sub_task2():
    while True:
        print("sub task2 is running")
        time.sleep(1)
        break


t1=threading.Thread(target=sub_task1,args=())
t2=threading.Thread(target=sub_task2)

t1.start()
t2.start()
t1.join()
t2.join()
print("main thread executed")

