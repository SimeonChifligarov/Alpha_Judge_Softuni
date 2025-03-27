def decode_morse(data: str, morse_dict: dict[str, str]) -> str:
    """Decodes a Morse code message into an alphabetic string."""
    words = data.split(' | ')
    decoded_words = []

    for word in words:
        decoded_word = ''.join(morse_dict[char] for char in word.strip().split())
        decoded_words.append(decoded_word)

    return ' '.join(decoded_words)


if __name__ == '__main__':
    morse_code = [
        '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
        '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..'
    ]
    alphabet = [chr(65 + i) for i in range(26)]
    dict_morse_to_alpha = {morse_code[i]: alphabet[i] for i in range(len(morse_code))}

    data_input: str = input().strip()

    result: str = decode_morse(data_input, dict_morse_to_alpha)
    print(result)
