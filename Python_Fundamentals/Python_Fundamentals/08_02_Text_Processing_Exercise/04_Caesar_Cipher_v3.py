def encrypt_message(message: str) -> str:
    """Encrypts the message by shifting each character forward by 3 ASCII positions."""
    return ''.join(chr(ord(char) + 3) for char in message)


if __name__ == '__main__':
    message_input: str = input().strip()

    encrypted_message: str = encrypt_message(message_input)
    print(encrypted_message)
