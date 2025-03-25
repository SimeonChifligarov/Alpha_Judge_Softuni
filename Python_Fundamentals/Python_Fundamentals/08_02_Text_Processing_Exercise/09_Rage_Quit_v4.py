import re


def process_rage_message(text: str) -> None:
    """Processes the input text to generate the rage message and print unique symbol count."""
    matches = re.findall(r'(\D+)(\d+)', text)

    rage_message = ''.join(letters.upper() * int(number) for letters, number in matches)
    unique_symbols = len(set(rage_message))

    print(f'Unique symbols used: {unique_symbols}')
    print(rage_message)


if __name__ == '__main__':
    input_text = input()
    process_rage_message(text=input_text)
