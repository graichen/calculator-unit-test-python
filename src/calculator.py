
class Calculator:
    def __init__(self):
        return

    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b

    @staticmethod
    def divide(a, b):
        return a / b

    @staticmethod
    def multiply(a, b):
        return a * b


if __name__ == "__main__":
    print('3 + 5 = ', Calculator.sum(3, 5))
    print('12 - 3.5 = ', Calculator.minus(12, 3.5))
    print('525 / 25 = ', Calculator.divide(525, 25))
    print('17 * 3.14159 = ', Calculator.multiply(17, 3.14159))
    print('53.22 - 69.32 = ', Calculator.minus(53.22, 69.32))
