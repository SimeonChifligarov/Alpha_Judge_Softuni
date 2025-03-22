def encrypt_text(input_text: str) -> str:
    """
    Encrypts the given text by shifting each character three positions forward in the ASCII table.
    Returns the encrypted text.
    """
    encrypted_chars: list[str] = []

    for char in input_text:
        ascii_value: int = ord(char)
        shifted_ascii_value: int = ascii_value + 3
        encrypted_char: str = chr(shifted_ascii_value)
        encrypted_chars.append(encrypted_char)

    encrypted_text: str = ''.join(encrypted_chars)
    return encrypted_text


if __name__ == '__main__':
    user_input: str = input()
    encrypted_result: str = encrypt_text(input_text=user_input)
    print(encrypted_result)
