def merge_strings(strings: list[str], start_index: int, end_index: int) -> list[str]:
    """
    Merges elements in the given list from start_index to end_index.
    """
    start_index = max(0, start_index)
    end_index = min(len(strings) - 1, end_index)

    if start_index <= end_index:
        merged_string = ''.join(strings[start_index:end_index + 1])
        # del strings[start_index:end_index + 1]
        # strings.insert(start_index, merged_string)
        strings = strings[:start_index] + [merged_string] + strings[end_index + 1:]

    return strings


def divide_string(strings: list[str], index: int, partitions: int) -> list[str]:
    """
    Divides the element at index into the specified number of partitions.
    """
    if 0 <= index < len(strings) and partitions > 0:
        string_to_divide = strings[index]
        segment_length = len(string_to_divide) // partitions
        # extra_chars = len(string_to_divide) % partitions
        new_parts = []

        # start = 0
        for i in range(partitions - 1):
            # end = start + segment_length + (1 if i < extra_chars else 0)  # TODO: FIX MISTAKE!
            # new_parts.append(string_to_divide[start:end])
            # start = end

            new_parts.append(string_to_divide[:segment_length])
            string_to_divide = string_to_divide[segment_length:]
        new_parts.append(string_to_divide)

        strings = strings[:index] + new_parts + strings[index + 1:]

    return strings


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
            strings = merge_strings(strings=strings, start_index=int(parts[1]), end_index=int(parts[2]))
        elif action == 'divide':
            strings = divide_string(strings=strings, index=int(parts[1]), partitions=int(parts[2]))

    return ' '.join(strings)


if __name__ == '__main__':
    data = input().split()
    print(process_commands(strings=data))
