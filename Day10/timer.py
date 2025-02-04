import threading
import time

def timer():
    seconds = 0
    while True:
        time.sleep(1)  
        seconds += 1
        
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        sec = seconds % 60
        
        print(f"Time elapsed: {hours:02d}:{minutes:02d}:{sec:02d}", end="\r") 
         
timer_thread = threading.Thread(target=timer, daemon=True)
timer_thread.start()

try:
    while True:
        time.sleep(1)  
        
except KeyboardInterrupt:
    print("\nTimer stopped.")