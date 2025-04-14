def get_unique_names(count_names: int) -> set:
    """
    This function gets unique names from user input.

    Args:
        count_names (int): How many names to read

    Returns:
        set: A set with all the different names
    """
    names_list = [input() for _ in range(count_names)]
    names_set = set(names_list)
    return names_set


if __name__ == '__main__':
    input_count = int(input())
    unique_names = get_unique_names(count_names=input_count)
    print(*unique_names, sep='\n')
