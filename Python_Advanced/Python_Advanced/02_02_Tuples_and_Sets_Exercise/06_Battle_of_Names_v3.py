def handle_name_ascii(count_names: int) -> set:
    """
    This function handles names, calculates special values and finds final set.

    Args:
        count_names (int): How many names will be given

    Returns:
        set: The final set after comparing sums
    """
    odd_set = set()
    even_set = set()
    names_list = [input() for _ in range(count_names)]
    for index, current_name in enumerate(names_list, start=1):
        value_sum = sum(ord(symbol) for symbol in current_name) // index
        (odd_set if value_sum % 2 else even_set).add(value_sum)
    sum_odd = sum(odd_set)
    sum_even = sum(even_set)
    if sum_odd == sum_even:
        return odd_set | even_set
    if sum_odd > sum_even:
        return odd_set - even_set
    return odd_set ^ even_set


if __name__ == '__main__':
    input_lines = int(input())
    output_set = handle_name_ascii(count_names=input_lines)
    print(', '.join(str(element) for element in output_set))
