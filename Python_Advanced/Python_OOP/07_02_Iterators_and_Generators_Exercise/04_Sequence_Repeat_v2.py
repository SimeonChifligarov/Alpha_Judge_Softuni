class sequence_repeat:
    """
    This class makes an iterator that repeats a sequence
    until it reaches a needed total number of characters.

    Args:
        sequence (str): The string to repeat.
        count (int): How many characters to produce.
    """

    def __init__(self, sequence: str, count: int) -> None:
        self.sequence = sequence
        self.count = count
        self.index = 0
        self.sequence_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.count:
            raise StopIteration
        if self.sequence_index >= len(self.sequence):
            self.sequence_index = 0
        current_char = self.sequence[self.sequence_index]
        self.sequence_index += 1
        self.index += 1
        return current_char


if __name__ == '__main__':
    # result_instance = sequence_repeat(sequence='abc', count=5)
    # for item in result_instance:
    #     print(item, end='')
    #
    # result_instance = sequence_repeat(sequence='I Love Python', count=3)
    # for item in result_instance:
    #     print(item, end='')
    pass
