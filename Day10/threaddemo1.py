import threading    #1
import time         #2

print("main thread execution started")

def single_task():
    print("sub task started")#4
    time.sleep(2) #5
    print("sub task completed")#6

thread=threading.Thread(target=single_task)#3
thread.start()#4
thread.join()#7
print("main thread execution completed")#8
    