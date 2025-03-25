def decode_rage_message(data: str) -> str:
    """Decodes a rage message where numbers indicate repetition of preceding characters."""
    data = data.upper()
    current_string = ''
    total_string = ''
    index = 0

    while index < len(data):
        if not data[index].isdigit():
            current_string += data[index]
        else:
            number_of_repeats = 0
            while index < len(data) and data[index].isdigit():
                number_of_repeats = number_of_repeats * 10 + int(data[index])
                index += 1

            total_string += current_string * number_of_repeats
            current_string = ''
            continue

        index += 1

    return total_string


if __name__ == '__main__':
    data_input: str = input().strip()

    result: str = decode_rage_message(data_input)

    print(f'Unique symbols used: {len(set(result))}')
    print(result)
