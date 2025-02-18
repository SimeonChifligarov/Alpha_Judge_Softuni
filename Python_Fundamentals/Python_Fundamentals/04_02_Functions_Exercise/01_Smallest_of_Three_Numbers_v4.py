def get_smallest_number(num_1: int, num_2: int, num_3: int) -> int:
    """
    Returns the smallest of three given integers.
    """
    return min(num_1, num_2, num_3)


if __name__ == '__main__':
    val_1 = int(input())
    val_2 = int(input())
    val_3 = int(input())
    result = get_smallest_number(num_1=val_1, num_2=val_2, num_3=val_3)
    print(result)
