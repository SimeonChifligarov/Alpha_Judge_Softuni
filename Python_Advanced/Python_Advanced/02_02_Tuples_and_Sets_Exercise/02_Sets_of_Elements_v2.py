def find_common_elements(length_first: int, length_second: int) -> set:
    """
    This function finds elements that are in both sets.

    Args:
        length_first (int): How many elements in first set
        length_second (int): How many elements in second set

    Returns:
        set: A set with elements that appear in both sets
    """
    first_set = {input() for _ in range(length_first)}
    second_set = {input() for _ in range(length_second)}
    common_set = first_set & second_set
    return common_set


if __name__ == '__main__':
    inputs_list = [int(el) for el in input().split()]
    n_value = inputs_list[0]
    m_value = inputs_list[1]
    common_elements = find_common_elements(length_first=n_value, length_second=m_value)
    for element in common_elements:
        print(element)
