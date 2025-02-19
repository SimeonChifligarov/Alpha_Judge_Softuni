def sum_even_odd_digits(number: int) -> tuple[int, int]:
    """
    Returns the sum of even and odd digits in the given number as a tuple.
    """
    odd_sum, even_sum = 0, 0
    for digit in str(abs(number)):
        num = int(digit)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return odd_sum, even_sum


if __name__ == '__main__':
    input_number = int(input())
    odd_result, even_result = sum_even_odd_digits(number=input_number)
    print(f'Odd sum = {odd_result}, Even sum = {even_result}')
