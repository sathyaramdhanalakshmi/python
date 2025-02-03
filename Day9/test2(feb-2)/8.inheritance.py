class Animal:
    def speak(self):
        print(f"animal speaks")
        
class Cat(Animal):
    def speak(self):
        print(f"cat speaks meows")
        
class Dog(Animal):
    def speak(self):
        print(f"dog speaks barks")
        
obj1=Dog()
obj1.speak()
 
obj2=Cat()
obj2.speak()