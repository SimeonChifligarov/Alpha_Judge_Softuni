def is_perfect_number(number: int) -> str:
    """
    Checks if the given number is a perfect number and returns an appropriate message.
    """
    divisors_sum = sum(divisor for divisor in range(1, number) if number % divisor == 0)
    return 'We have a perfect number!' if divisors_sum == number else 'It\'s not so perfect.'


if __name__ == '__main__':
    input_number = int(input())
    result = is_perfect_number(number=input_number)
    print(result)
