def encrypt_text(input_text: str) -> str:
    """
    Encrypts the given text by shifting each character three positions forward in the ASCII table.
    Returns the encrypted text.
    """
    return ''.join(chr(ord(char) + 3) for char in input_text)


if __name__ == '__main__':
    user_input: str = input()
    encrypted_result: str = encrypt_text(input_text=user_input)
    print(encrypted_result)
