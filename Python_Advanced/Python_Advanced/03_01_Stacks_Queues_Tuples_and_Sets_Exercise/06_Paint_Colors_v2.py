from collections import deque


def find_colors(parts: list[str]) -> None:
    """
    This function finds all possible colors by combining parts of a string.

    Args:
        parts (list[str]): List with string parts.

    Returns:
        None
    """
    substrings = deque(parts)
    collected_colors = []
    main_colors = {'red', 'yellow', 'blue'}
    secondary_colors = {
        'orange': {'red', 'yellow'},
        'purple': {'red', 'blue'},
        'green': {'yellow', 'blue'},
    }
    while substrings:
        if len(substrings) == 1:
            first = substrings.pop()
            second = ''
        else:
            first = substrings.popleft()
            second = substrings.pop()
        combined = first + second
        combined_reverse = second + first
        if combined in main_colors or combined in secondary_colors:
            collected_colors.append(combined)
        elif combined_reverse in main_colors or combined_reverse in secondary_colors:
            collected_colors.append(combined_reverse)
        else:
            if first[:-1]:
                index = len(substrings) // 2
                substrings.insert(index, first[:-1])
            if second[:-1]:
                index = len(substrings) // 2
                substrings.insert(index, second[:-1])
    final_colors = []
    for color in collected_colors:
        if color in main_colors:
            final_colors.append(color)
        else:
            needed = secondary_colors[color]
            if needed.issubset(set(collected_colors)):
                final_colors.append(color)
    print(final_colors)


if __name__ == '__main__':
    substrings_input = input().split()
    find_colors(parts=substrings_input)
