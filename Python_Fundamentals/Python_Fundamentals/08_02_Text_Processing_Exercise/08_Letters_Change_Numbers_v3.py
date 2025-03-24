def letter_position(letter: str) -> int:
    """Returns the position of a letter in the alphabet (A=1, B=2, ..., Z=26)."""
    return ord(letter.lower()) - ord('a') + 1


def process_string(segment: str) -> float:
    """Processes a single string segment according to given rules and returns the result."""
    first_letter, number, last_letter = segment[0], int(segment[1:-1]), segment[-1]

    if first_letter.isupper():
        number /= letter_position(first_letter)
    else:
        number *= letter_position(first_letter)

    if last_letter.isupper():
        number -= letter_position(last_letter)
    else:
        number += letter_position(last_letter)

    return number


def calculate_total_sum(text: str) -> float:
    """Calculates the total sum of all processed numbers in a given text."""
    segments = text.split()
    return sum(process_string(segment) for segment in segments)


if __name__ == '__main__':
    input_text = input()
    total_sum = calculate_total_sum(text=input_text)
    print(f'{total_sum:.2f}')
