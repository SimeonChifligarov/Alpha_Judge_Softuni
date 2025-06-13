def fibonacci():
    """
    This function gives Fibonacci numbers one by one.
    Yields:
        int: next number in Fibonacci sequence
    """
    previous, current = 0, 1
    while True:
        yield previous
        previous, current = current, previous + current

# if __name__ == '__main__':
#     # generator = fibonacci()
#     # for _ in range(5):
#     #     print(next(generator))
#     pass
