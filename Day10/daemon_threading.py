import threading
import time

def background_task():
    
    while True:
        print("Daemon thread is running...")
        time.sleep(1)

daemon_thread = threading.Thread(target=background_task, daemon=True)
daemon_thread.start()

print("Main thread is running")

time.sleep(3)
print("Main thread is exiting")