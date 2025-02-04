import threading
import queue
import time

def producer(que):
    for item in range(5):
        time.sleep(2)
        que.put(item)
        print(f"produced : {item}")
        
def consumer(q):
    while True:
        item=que.get()
        if item is None:
            break
        print(f"consumed : {item}")
        time.sleep(2)
        
que=queue.Queue()
producer_thread=threading.Thread(target=producer,args=(que,))
consumer_thread=threading.Thread(target=consumer,args=(que,))

producer_thread.start()
consumer_thread.start()
producer_thread.join()
que.put(None)
consumer_thread.join()

print("thread communication is completed")
