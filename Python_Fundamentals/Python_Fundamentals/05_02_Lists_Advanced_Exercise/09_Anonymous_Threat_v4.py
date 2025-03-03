def merge_strings(strings: list[str], start_index: int, end_index: int) -> None:
    """
    Merges elements in the given list from start_index to end_index.
    """
    start_index = max(0, start_index)
    end_index = min(len(strings) - 1, end_index)

    if start_index <= end_index:
        merged_string = ''.join(strings[start_index:end_index + 1])
        del strings[start_index:end_index + 1]
        strings.insert(start_index, merged_string)


def divide_string(strings: list[str], index: int, partitions: int) -> None:
    """
    Divides the element at index into the specified number of partitions.
    """
    if 0 <= index < len(strings) and partitions > 0:
        string_to_divide = strings[index]
        segment_length = len(string_to_divide) // partitions
        new_parts = []

        start = 0
        for i in range(partitions):
            end = start + segment_length if i < partitions - 1 else None
            new_parts.append(string_to_divide[start:end])
            start = end

        strings[index:index + 1] = new_parts


def process_commands(strings: list[str]) -> str:
    """
    Processes merge and divide commands until '3:1' is received.
    """
    while True:
        command = input()
        if command == '3:1':
            break

        parts = command.split()
        action = parts[0]

        if action == 'merge':
            merge_strings(strings=strings, start_index=int(parts[1]), end_index=int(parts[2]))
        elif action == 'divide':
            divide_string(strings=strings, index=int(parts[1]), partitions=int(parts[2]))

    return ' '.join(strings)


if __name__ == '__main__':
    data = input().split()
    print(process_commands(strings=data))
