class Calculator:
    """This class helps you do basic math: adding, multiplying, dividing and subtracting."""

    @staticmethod
    def add(*numbers: float) -> float:
        return sum(numbers)

    @staticmethod
    def multiply(*numbers: float) -> float:
        result: float = 1
        for value in numbers:
            result *= value
        return result

    @staticmethod
    def divide(*numbers: float) -> float:
        if not numbers:
            return 0
        result: float = numbers[0]
        for value in numbers[1:]:
            if value == 0:
                return 0
            result /= value
        return result

    @staticmethod
    def subtract(*numbers: float) -> float:
        if not numbers:
            return 0
        result: float = numbers[0]
        for value in numbers[1:]:
            result -= value
        return result


if __name__ == '__main__':
    # print(Calculator.add(5, 10, 4))
    # print(Calculator.multiply(1, 2, 3, 5))
    # print(Calculator.divide(100, 2))
    # print(Calculator.subtract(90, 20, -50, 43, 7))
    pass
