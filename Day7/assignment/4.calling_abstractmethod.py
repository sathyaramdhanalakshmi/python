from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def profession(self):
        pass

    def introduce(self):
        print("I am a father.")
        self.profession()

class Engineer(Father):
    def profession(self):
        print("I am an Engineer.")

class Doctor(Father):
    def profession(self):
        print("I am a Doctor.")

e = Engineer()
e.introduce()

d = Doctor()
d.introduce()