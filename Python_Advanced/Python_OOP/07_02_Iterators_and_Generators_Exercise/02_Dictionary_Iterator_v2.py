class dictionary_iter:
    """
    This class makes an iterator that gives each key and value
    from a dictionary as a tuple with two elements.

    Args:
        data (dict): The dictionary to iterate.
    """

    def __init__(self, data: dict) -> None:
        self.data = list(data.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        current_pair = self.data[self.index]
        self.index += 1
        return current_pair


if __name__ == '__main__':
    # result_instance = dictionary_iter(data={1: '1', 2: '2'})
    # for element in result_instance:
    #     print(element)
    #
    # result_instance = dictionary_iter(data={'name': 'Peter', 'age': 24})
    # for element in result_instance:
    #     print(element)
    pass
