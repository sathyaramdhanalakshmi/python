from abc import ABC, abstractmethod

class Mail(ABC):
    @abstractmethod
    def send(self):
        pass

class Email(Mail):
    def send(self):
        print("sendinging mail through Email")

class SMS(Mail):
    def send(self):
        print("sending mail through SMS")

class Whatsapp(Mail):
    def send(self):
        print("sending mail through whatsapp")

obj1=Email()
obj1.send()

obj2=SMS()
obj2.send()

obj3=Whatsapp()
obj3.send()
        

