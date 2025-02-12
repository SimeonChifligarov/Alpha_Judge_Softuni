def create_message(numbers: str, text: str) -> str:
    """
    Constructs a message using characters from the text based on the indices calculated
    by summing the digits of each number in the sequence.
    """

    indices = [sum(int(digit) for digit in num) for num in numbers.split()]
    message = ''

    for index in indices:
        adjusted_index = index % len(text)
        message += text[adjusted_index]
        text = text[:adjusted_index] + text[adjusted_index + 1:]
    return message


if __name__ == '__main__':
    sequence = input()
    input_string = input()
    result = create_message(numbers=sequence, text=input_string)
    print(result)
