# 70_calculator_class:

class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
        
    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2
    
calculator = Calculator(20000000,100000)
print(calculator.divide())
print(calculator.multiply())
print(calculator.add())
print(calculator.subtract())
