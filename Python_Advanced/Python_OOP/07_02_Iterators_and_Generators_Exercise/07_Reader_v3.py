from typing import Any, Iterable


class Reader:
    """
    This class gives a generator for items from many collections.
    """

    def __init__(self) -> None:
        pass

    def __call__(self, *collections: Iterable[Any]):
        return self.read_next(*collections)

    def __str__(self) -> str:
        return 'Reader that reads from many iterables'

    def __repr__(self) -> str:
        return 'Reader()'

    def read_next(self, *collections: Iterable[Any]):
        """
        This function gives one item at a time from each given collection.
        Args:
            *collections (Iterable[Any]): any number of iterables
        Yields:
            Any: next item from collections
        """
        for collection in collections:
            for element in collection:
                yield element


read_next = Reader().read_next

if __name__ == '__main__':
    # generator_instance = read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4})
    # for item in generator_instance:
    #     print(item, end='')
    # generator_instance = read_next('Need', (2, 3), ['words', '.'])
    # for item in generator_instance:
    #     print(item)
    pass
