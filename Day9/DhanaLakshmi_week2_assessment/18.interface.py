from abc import ABC

class ICalculator(ABC):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b


class BasicCalculator(ICalculator):
    pass 


calc = BasicCalculator()

print(f"Addition: {calc.add(10, 5)}")
print(f"Subtraction: {calc.subtract(10, 5)}")
print(f"Multiplication: {calc.multiply(10, 5)}")
print(f"Division: {calc.divide(10, 5)}")
print(f"Division by zero: {calc.divide(10, 0)}")
