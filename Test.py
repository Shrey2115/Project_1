class Calculator:
    def __init__(self):
        pass
    # This directly compares to a constructor in Java 

    def add(self, num1, num2):
        print(num1 + num2)

    def multiply(self, num1, num2):
        print(num1 * num2)

    def subtract(self, num1, num2):
        print(num1 - num2)

    def divide(self, num1, num2):
        print(num1/(num2 * 1.0))

    # python methods except here you don't specify the return type of the method and one of the arguments of the method is the instance of the class itself


calc = Calculator()

calc.add(1,2)