class Logger:
    
    def log(self, message, level="info"):
        if level.lower()== "error":
            print(f"[ERROR]: {message}")
        elif level.lower()=="warning":
            print(f"[warning]: {message}")
        else:
            print(f"[info]: {message}")
            
obj=Logger()
obj.log("system started")
obj.log("Low disk space", "warming")
obj.log("File not found", "error")
        