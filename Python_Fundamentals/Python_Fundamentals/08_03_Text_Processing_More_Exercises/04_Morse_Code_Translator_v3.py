def morse_to_english(morse_message: str) -> str:
    """
    Translates a Morse code message to English (capital letters).

    :param morse_message: The Morse code message with letters separated by spaces and words by ' | '.
    :return: The translated English message.
    """
    morse_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z',
    }

    words = morse_message.split(' | ')
    translated_words = [''.join(morse_dict[letter] for letter in word.split()) for word in words]

    return ' '.join(translated_words)


if __name__ == '__main__':
    morse_code_input = input()
    result = morse_to_english(morse_message=morse_code_input)
    print(result)
