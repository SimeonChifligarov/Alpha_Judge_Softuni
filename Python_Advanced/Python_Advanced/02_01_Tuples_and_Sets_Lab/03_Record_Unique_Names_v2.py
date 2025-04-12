def get_unique_names(names_list: list[str]) -> list[str]:
    """
    Get only unique names from the list.

    Args:
        names_list (list[str]): List with names.

    Returns:
        set[str]: Set with unique names.
    """
    unique_names_set = set()
    for name in names_list:
        unique_names_set.add(name)
    return list(unique_names_set)


if __name__ == '__main__':
    names_count = int(input())
    names_input = [input() for _ in range(names_count)]
    unique_names_output = get_unique_names(names_list=names_input)
    for n in unique_names_output:
        print(n)
