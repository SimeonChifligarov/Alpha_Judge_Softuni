class FibonacciGenerator:
    """
    This class makes Fibonacci numbers forever.
    """

    def __init__(self) -> None:
        pass

    def __call__(self):
        return self.fibonacci()

    def __str__(self) -> str:
        return 'FibonacciGenerator infinite sequence'

    def __repr__(self) -> str:
        return 'FibonacciGenerator()'

    def fibonacci(self):
        """
        This function gives Fibonacci numbers forever.
        Yields:
            int: next Fibonacci number
        """
        value_1, value_2 = 0, 1
        while True:
            yield value_1
            value_1, value_2 = value_2, value_1 + value_2


fibonacci = FibonacciGenerator().fibonacci

# if __name__ == '__main__':
#     generator_instance = fibonacci()
#     for index in range(5):
#         print(next(generator_instance))
#     generator_instance = fibonacci()
#     for index in range(1):
#         print(next(generator_instance))
#     pass
