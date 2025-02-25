def sort_names(names: list[str]) -> list[str]:
    """
    Sorts the given list of names by length in descending order.
    If names have the same length, they are sorted alphabetically in ascending order.
    """
    return sorted(names, key=lambda name: (-len(name), name))


if __name__ == '__main__':
    names_input = input().split(', ')
    sorted_names = sort_names(names=names_input)
    print(sorted_names)
