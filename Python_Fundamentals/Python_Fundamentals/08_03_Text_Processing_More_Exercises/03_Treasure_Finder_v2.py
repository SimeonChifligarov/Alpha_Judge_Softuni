def decrypt_message(data: str, key: list[int]) -> str:
    """Decrypts a message by subtracting values from `key` in a cyclic manner."""
    real_message = []
    key_length = len(key)

    for index, char in enumerate(data):
        real_message.append(chr(ord(char) - key[index % key_length]))

    return ''.join(real_message)


def extract_treasure_info(decrypted_message: str) -> tuple[str, str]:
    """Extracts treasure type and location from the decrypted message."""
    start_index_type = decrypted_message.index('&') + 1
    end_index_type = decrypted_message.index('&', start_index_type)
    treasure_type = decrypted_message[start_index_type:end_index_type]

    start_index_location = decrypted_message.index('<') + 1
    end_index_location = decrypted_message.index('>', start_index_location)
    location = decrypted_message[start_index_location:end_index_location]

    return treasure_type, location


if __name__ == '__main__':
    key: list[int] = [int(el) for el in input().split()]

    while True:
        data: str = input().strip()
        if data == 'find':
            break

        decrypted_message: str = decrypt_message(data, key)
        treasure_type, location = extract_treasure_info(decrypted_message)

        print(f'Found {treasure_type} at {location}')
