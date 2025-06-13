class GeneratorHelpers:
    """
    This class gives helpers: take, halves, integers.
    """

    def __init__(self) -> None:
        pass

    def __call__(self):
        return self.take, self.halves, self.integers

    def __str__(self) -> str:
        return 'GeneratorHelpers for taking halves of integers'

    def __repr__(self) -> str:
        return 'GeneratorHelpers()'

    def integers(self):
        """
        This function makes infinite numbers starting from 1.
        Yields:
            int: next integer starting from 1
        """
        value = 1
        while True:
            yield value
            value += 1

    def halves(self):
        """
        This function gives half of each integer.
        Yields:
            float: half of next integer
        """
        for element in self.integers():
            yield element / 2

    def take(self, elements_count: int, source) -> list:
        """
        This function takes first elements_count elements from source.
        Args:
            elements_count (int): how many elements to take
            source (Iterator): where to take elements from
        Returns:
            list: list of elements taken
        """
        if elements_count <= 0:
            return []
        return [next(source) for _ in range(elements_count)]


solution = GeneratorHelpers()

# if __name__ == '__main__':
#     take_func = solution()[0]
#     halves_func = solution()[1]
#     output = take_func(elements_count=5, source=halves_func())
#     print(output)
#     output = take_func(elements_count=0, source=halves_func())
#     print(output)
#     pass
