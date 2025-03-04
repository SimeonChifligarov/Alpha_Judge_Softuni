def extract_hidden_message(text: str) -> str:
    """
    Extracts a hidden message from the given text by separating digits and non-digits,
    then using the digits to determine how many characters to take and skip.
    """
    numbers = [int(char) for char in text if char.isdigit()]
    non_numbers = [char for char in text if not char.isdigit()]

    take_list = numbers[::2]
    skip_list = numbers[1::2]

    result = []
    index = 0

    for take, skip in zip(take_list, skip_list):
        result.extend(non_numbers[index:index + take])
        index += take + skip

    return ''.join(result)


if __name__ == '__main__':
    input_text = input()
    output_message = extract_hidden_message(text=input_text)
    print(output_message)
