import re


def decrypt_message(key: list[int], encrypted_text: str) -> str:
    """
    Decrypts a message by reducing each character's ASCII value using a repeating key sequence.

    :param key: List of integers used for decryption.
    :param encrypted_text: The encrypted message.
    :return: The decrypted message.
    """
    key_length = len(key)
    return ''.join(chr(ord(char) - key[i % key_length]) for i, char in enumerate(encrypted_text))


def extract_treasure_info(decrypted_text: str) -> tuple[str, str]:
    """
    Extracts the treasure type and coordinates from the decrypted message.

    :param decrypted_text: The decrypted message.
    :return: A tuple containing the treasure type and its coordinates.
    """
    treasure_type = re.search(r'&(.+?)&', decrypted_text).group(1)
    coordinates = re.search(r'<(.+?)>', decrypted_text).group(1)
    return treasure_type, coordinates


if __name__ == '__main__':
    key_sequence = [int(num) for num in input().split()]
    while True:
        encrypted_line = input()
        if encrypted_line == 'find':
            break

        decrypted_line = decrypt_message(key=key_sequence, encrypted_text=encrypted_line)
        treasure, coords = extract_treasure_info(decrypted_text=decrypted_line)
        print(f'Found {treasure} at {coords}')
