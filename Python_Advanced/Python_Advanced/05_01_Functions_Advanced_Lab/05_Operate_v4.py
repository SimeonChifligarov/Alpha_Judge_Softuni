def operate(symbol: str, *numbers: int) -> float:
    """
    This function uses a math symbol to do an operation over many numbers.

    Args:
        symbol (str): The math symbol to use.
        *numbers (int): The numbers to use in the operation.

    Returns:
        float: The final answer after applying the operation.
    """

    def add() -> int:
        return sum(numbers)

    def subtract() -> int:
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result

    def multiply() -> int:
        result = 1
        for num in numbers:
            result *= num
        return result

    def divide() -> float:
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                continue
            result /= num
        return result

    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }
    return operations[symbol]()

# if __name__ == '__main__':
#     operation_input = input()
#     nums_input = [int(x) for x in input().split()]
#     operation_result = operate(symbol=operation_input, *nums_input)
#     print(operation_result)
