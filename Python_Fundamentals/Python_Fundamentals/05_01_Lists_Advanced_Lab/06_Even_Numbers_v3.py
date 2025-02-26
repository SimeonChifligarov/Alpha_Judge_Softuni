def get_even_indices():
    """
    Reads a string of numbers separated by ', ',
    finds the indices of all even numbers, and prints them.
    """
    numbers = map(int, input().split(', '))
    even_indices = [index for index, num in enumerate(numbers) if num % 2 == 0]

    print(even_indices)


if __name__ == '__main__':
    get_even_indices()
