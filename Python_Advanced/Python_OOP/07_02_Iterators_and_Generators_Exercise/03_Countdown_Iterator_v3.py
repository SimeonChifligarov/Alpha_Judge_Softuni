class countdown_iterator:
    """
    This class makes an iterator that counts down
    from a given number to zero.

    Args:
        start (int): The number to start the countdown from.
    """

    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        current_value = self.current
        self.current -= 1
        return current_value

    def __str__(self) -> str:
        return f'countdown_iterator(start={self.current})'

    def __repr__(self) -> str:
        return f'countdown_iterator(start={self.current})'


if __name__ == '__main__':
    # iterator_instance = countdown_iterator(start=10)
    # for item in iterator_instance:
    #     print(item, end=' ')
    #
    # iterator_instance = countdown_iterator(start=0)
    # for item in iterator_instance:
    #     print(item, end=' ')
    pass
