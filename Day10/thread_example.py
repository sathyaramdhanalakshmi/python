import threading  #1
import time   #2

print("main thread execution started")
def employee1():
    print("developer")
    time.sleep(2)
    print("manager is coding")
    
def employee2():
    print("tester")#4
    time.sleep(2) #5
    print("tester is testing the code")#6

thread=threading.Thread(target=employee1)#3


thread.start()#4
thread.join()#7
print("code is tested")#8
    