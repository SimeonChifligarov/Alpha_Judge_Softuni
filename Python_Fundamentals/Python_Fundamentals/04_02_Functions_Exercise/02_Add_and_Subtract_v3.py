def sum_numbers(val_1: int, val_2: int) -> int:
    """
    Returns the sum of the first two integers.
    """
    return val_1 + val_2


def subtract(total: int, val_3: int) -> int:
    """
    Returns the difference between the given sum and the third integer.
    """
    return total - val_3


def add_and_subtract(num_1: int, num_2: int, num_3: int) -> int:
    """
    Returns the final result by summing the first two numbers and subtracting the third.
    """
    return subtract(total=sum_numbers(val_1=num_1, val_2=num_2), val_3=num_3)


if __name__ == '__main__':
    inp_1 = int(input())
    inp_2 = int(input())
    inp_3 = int(input())
    output = add_and_subtract(num_1=inp_1, num_2=inp_2, num_3=inp_3)
    print(output)
