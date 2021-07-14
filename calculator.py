class Calculator:
    def addition(self, a, b):
        if not isinstance(a, int):
            raise Exception
        return a+b

    def subtraction(self, a, b):
        return a-b

    def multiply(self, a, b):
        return a*b

    def division(self, a, b):
        return a/b
