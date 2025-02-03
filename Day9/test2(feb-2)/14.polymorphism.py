class Notification:
    def send_message(self, message):
        print(f"Sending notification: {message}")

class Email_Notification(Notification):
    def send_message(self, message):  
        print(f"Sending Email: {message}")


class SMS_Notification(Notification):
    def send_message(self, message):  
        print(f"Sending SMS: {message}")


obj1 = Email_Notification()
obj1.send_message("Hello via Email!")  

obj2 = SMS_Notification()
obj2.send_message("Hello via SMS!")  