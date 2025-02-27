def find_repeating_substrings():
    """
    Reads two comma-separated lists of strings.
    Identifies and prints unique elements from the first list
    that appear as substrings in any element of the second list.
    """
    first_list = input().split(', ')
    second_list = input().split(', ')

    repeated_elements = {word for word in first_list if any(word in second for second in second_list)}

    print(sorted(repeated_elements, key=first_list.index))


if __name__ == '__main__':
    find_repeating_substrings()
