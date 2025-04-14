def get_repeated_elements(size_one: int, size_two: int) -> set:
    """
    This function gets the elements that are in both sets.

    Args:
        size_one (int): Number of elements in the first set
        size_two (int): Number of elements in the second set

    Returns:
        set: A set with the repeated elements
    """
    set_one = {input() for _ in range(size_one)}
    set_two = {input() for _ in range(size_two)}
    repeated_elements = set_one.intersection(set_two)
    return repeated_elements


if __name__ == '__main__':
    numbers_input = [int(el) for el in input().split()]
    first_size = numbers_input[0]
    second_size = numbers_input[1]
    intersection_result = get_repeated_elements(size_one=first_size, size_two=second_size)
    for item in intersection_result:
        print(item)
