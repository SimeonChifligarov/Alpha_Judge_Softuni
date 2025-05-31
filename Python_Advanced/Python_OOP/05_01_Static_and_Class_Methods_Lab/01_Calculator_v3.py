class Calculator:
    """This class helps to do simple math operations like add, multiply, divide and subtract."""

    @staticmethod
    def add(*values: float) -> float:
        return sum(values)

    @staticmethod
    def multiply(*values: float) -> float:
        result: float = 1
        for element in values:
            result *= element
        return result

    @staticmethod
    def divide(*values: float) -> float:
        if not values:
            return 0
        result: float = values[0]
        for element in values[1:]:
            if element == 0:
                return 0
            result /= element
        return result

    @staticmethod
    def subtract(*values: float) -> float:
        if not values:
            return 0
        result: float = values[0]
        for element in values[1:]:
            result -= element
        return result

    def __str__(self) -> str:
        return 'Calculator class for basic math operations.'

    def __repr__(self) -> str:
        return 'Calculator()'


if __name__ == '__main__':
    # print(Calculator.add(5, 10, 4))
    # print(Calculator.multiply(1, 2, 3, 5))
    # print(Calculator.divide(100, 2))
    # print(Calculator.subtract(90, 20, -50, 43, 7))
    pass
