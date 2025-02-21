def factorial(num: int) -> int:
    """
    Returns the factorial of a given number.
    """
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


def divide_factorials(num_1: int, num_2: int) -> str:
    """
    Calculates the factorial of two numbers, divides the first by the second,
    and returns the result formatted to the second decimal point.
    """
    fact_1 = factorial(num=num_1)
    fact_2 = factorial(num=num_2)
    result = fact_1 / fact_2
    return f'{result:.2f}'


if __name__ == '__main__':
    input_num_1 = int(input())
    input_num_2 = int(input())
    res = divide_factorials(num_1=input_num_1, num_2=input_num_2)
    print(res)
