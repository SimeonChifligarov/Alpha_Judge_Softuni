def get_unique_chemicals(count_inputs: int) -> set:
    """
    This function finds all unique chemicals from the input.

    Args:
        count_inputs (int): How many lines of input

    Returns:
        set: A set with all unique chemical elements
    """
    all_elements = {element for _ in range(count_inputs) for element in input().split()}
    return all_elements


if __name__ == '__main__':
    total_lines = int(input())
    chemicals_result = get_unique_chemicals(count_inputs=total_lines)
    print('\n'.join(chemicals_result))
