class custom_range:
    """
    This class represents a custom range iterator.

    Args:
        start (int): The start of the range.
        end (int): The end of the range.
    """

    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self) -> 'custom_range':
        self.current = self.start
        return self

    def __next__(self) -> int:
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


if __name__ == '__main__':
    # one_to_ten = custom_range(start=1, end=10)
    # for num in one_to_ten:
    #     print(num)
    pass
