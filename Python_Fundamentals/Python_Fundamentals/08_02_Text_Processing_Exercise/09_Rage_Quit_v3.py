def generate_rage_message(text: str) -> tuple[int, str]:
    """Generates the rage message and counts unique symbols without using regular expressions."""
    rage_message = []
    current_text = ''
    current_number = ''

    for char in text:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                rage_message.append(current_text.upper() * int(current_number))
                current_text = ''
                current_number = ''
            current_text += char

    if current_number:
        rage_message.append(current_text.upper() * int(current_number))

    final_message = ''.join(rage_message)
    unique_symbols = len(set(final_message))

    return unique_symbols, final_message


if __name__ == '__main__':
    input_text = input()
    unique_count, message = generate_rage_message(text=input_text)
    print(f'Unique symbols used: {unique_count}')
    print(message)
