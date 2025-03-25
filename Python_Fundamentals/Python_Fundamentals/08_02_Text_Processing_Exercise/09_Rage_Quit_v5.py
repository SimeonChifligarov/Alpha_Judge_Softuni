import re


def generate_rage_message(text: str) -> tuple[int, str]:
    """Generates the rage message and counts unique symbols."""
    matches = re.findall(r'(\D+)(\d+)', text)

    rage_message = ''.join(letters.upper() * int(number) for letters, number in matches)
    unique_symbols = len(set(rage_message))

    return unique_symbols, rage_message


if __name__ == '__main__':
    input_text = input()
    unique_count, message = generate_rage_message(text=input_text)
    print(f'Unique symbols used: {unique_count}')
    print(message)
