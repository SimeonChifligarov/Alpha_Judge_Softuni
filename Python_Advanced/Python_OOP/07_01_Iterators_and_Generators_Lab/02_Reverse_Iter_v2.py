from typing import Iterable, Any


class reverse_iter:
    """
    This class represents a reverse iterator.

    Args:
        iterable (Iterable[Any]): The iterable to reverse.
    """

    def __init__(self, iterable: Iterable[Any]) -> None:
        self.items = list(iterable)
        self.index = len(self.items) - 1

    def __iter__(self) -> 'reverse_iter':
        return self

    def __next__(self) -> Any:
        if self.index < 0:
            raise StopIteration
        value = self.items[self.index]
        self.index -= 1
        return value


if __name__ == '__main__':
    # reversed_list = reverse_iter(iterable=[1, 2, 3, 4])
    # for item in reversed_list:
    #     print(item)
    pass
