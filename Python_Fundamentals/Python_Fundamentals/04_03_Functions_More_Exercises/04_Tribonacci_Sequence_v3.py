def tribonacci_sequence(n: int) -> list[int]:
    """
    Generates the first n numbers of the Tribonacci sequence and returns them as a list.

    :param n: The number of Tribonacci sequence terms to generate.
    :return: A list of the sequence.
    """
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    elif n == 3:
        return [1, 1, 2]

    seq = [1, 1, 2]

    for _ in range(n - 3):
        seq.append(seq[-1] + seq[-2] + seq[-3])

    return seq


if __name__ == '__main__':
    num_input = int(input())
    result = tribonacci_sequence(n=num_input)
    print(*result)
