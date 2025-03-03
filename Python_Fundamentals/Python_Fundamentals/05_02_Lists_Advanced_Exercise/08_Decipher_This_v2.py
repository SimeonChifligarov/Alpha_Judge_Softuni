def decipher_message(message: str) -> str:
    """
    Deciphers a secret message by switching the second and last letter of each word
    and replacing the first letter's character code with the corresponding character.
    """

    def decipher_word(word: str) -> str:
        first_part = ''.join([ch for ch in word if ch.isdigit()])
        remaining_part = ''.join([ch for ch in word if not ch.isdigit()])
        first_char = chr(int(first_part))

        if len(remaining_part) > 1:
            remaining_part = remaining_part[-1] + remaining_part[1:-1] + remaining_part[0]

        return first_char + remaining_part

    return ' '.join([decipher_word(word) for word in message.split()])


if __name__ == '__main__':
    secret_message = input()
    print(decipher_message(message=secret_message))
