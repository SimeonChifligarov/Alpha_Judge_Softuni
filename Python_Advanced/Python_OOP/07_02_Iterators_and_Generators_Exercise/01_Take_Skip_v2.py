class take_skip:
    """
    This class makes an iterator that gives numbers
    starting from 0, moving with a step, and stopping after a count.

    Args:
        step (int): How much to move after each number.
        count (int): How many numbers to give.
    """

    def __init__(self, step: int, count: int) -> None:
        self.step = step
        self.count = count
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= self.count:
            raise StopIteration
        value = self.current_index * self.step
        self.current_index += 1
        return value


if __name__ == '__main__':
    # numbers_instance = take_skip(2, 6)
    # for number in numbers_instance:
    #     print(number)
    pass
