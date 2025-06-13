def solution():
    """
    This function returns three helpers: take, halves, integers.
    """

    def integers():
        """
        This function makes infinite numbers starting from 1.
        Yields:
            int: next integer starting from 1
        """
        number = 1
        while True:
            yield number
            number += 1

    def halves():
        """
        This function gives half of each integer.
        Yields:
            float: half of next integer
        """
        for value in integers():
            yield value / 2

    def take(count: int, sequence) -> list:
        """
        This function takes first count elements from sequence.
        Args:
            count (int): how many elements to take
            sequence (Iterator): where to take elements from
        Returns:
            list: list of elements taken
        """
        if count <= 0:
            return []
        return [next(sequence) for _ in range(count)]

    return take, halves, integers


if __name__ == '__main__':
    # take_func, halves_func, integers_func = solution()
    # output = take_func(count=5, sequence=halves_func())
    # print(output)
    # output = take_func(count=0, sequence=halves_func())
    # print(output)
    pass
