def get_even_numbers(numbers: list[int]) -> list[int]:
    """
    Returns a list of even numbers from the given list.
    """
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers


if __name__ == '__main__':
    # input_numbers = list(map(int, input().split()))
    input_numbers = [int(el) for el in input().split()]
    result = get_even_numbers(numbers=input_numbers)
    print(result)
