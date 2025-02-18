def get_smallest_number(num_1: int, num_2: int, num_3: int) -> int:
    """
    Returns the smallest of three given integers.
    """
    if num_1 <= num_2 and num_1 <= num_3:
        return num_1
    elif num_2 <= num_1 and num_2 <= num_3:
        return num_2
    else:
        return num_3


if __name__ == '__main__':
    val_1 = int(input())
    val_2 = int(input())
    val_3 = int(input())
    result = get_smallest_number(num_1=val_1, num_2=val_2, num_3=val_3)
    print(result)
