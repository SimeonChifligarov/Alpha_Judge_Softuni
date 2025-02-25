def sort_names():
    """
    Reads a comma-separated list of names from user input,
    sorts them by length in descending order, and alphabetically for equal lengths.
    Prints the sorted list.
    """
    names = input().split(', ')

    sorted_names = sorted(names, key=lambda name: (-len(name), name))

    print(sorted_names)


if __name__ == "__main__":
    sort_names()
