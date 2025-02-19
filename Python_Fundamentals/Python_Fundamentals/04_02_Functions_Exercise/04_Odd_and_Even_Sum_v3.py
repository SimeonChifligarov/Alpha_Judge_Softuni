def sum_even_odd_digits(number: int) -> str:
    """
    Returns the sum of even and odd digits in the given number as a formatted string.
    """
    odd_sum = sum(int(digit) for digit in str(abs(number)) if int(digit) % 2 != 0)
    even_sum = sum(int(digit) for digit in str(abs(number)) if int(digit) % 2 == 0)
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


if __name__ == '__main__':
    input_number = int(input())
    result = sum_even_odd_digits(number=input_number)
    print(result)
