class Man:
    def __init__(self, manname):
        self.manname = manname

    def get_name(self):
        return self.manname

    def walk(self):
        return "Man should walk"

class Woman:
    def __init__(self, womanname):
        self.womanname = womanname  # Fixed the attribute name

    def get_name(self):
        return self.womanname  # Fixed incorrect attribute reference

    def bus(self):
        return "Women go in free bus"

class Both(Man, Woman):
    def __init__(self, manname, womanname):
        Man.__init__(self, manname)
        Woman.__init__(self, womanname)

    def cab(self):
        return "Both go in a cab"

# Correctly passing required arguments
obj = Both("John", "Alice")

print(obj.walk())  # Inherited from Man
print(obj.bus())   # Inherited from Women
print(obj.cab())   # Defined in Both
print(obj.get_name())  # Ambiguity: It will call Man's get_name() due to MRO

obj1 = Man("Dayanandh sharma")  # Correctly passing required argument
print(obj1.get_name())  # Output: David
obj2=Woman("sahithi")
print(obj2.get_name()) 