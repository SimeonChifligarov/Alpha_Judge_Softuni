def decrypt_message(key: int, n: int) -> str:
    message = ''
    for _ in range(n):
        char = input()
        message += chr(ord(char) + key)
    return message


if __name__ == '__main__':
    key_input = int(input())
    n_input = int(input())
    decrypted_message = decrypt_message(key=key_input, n=n_input)
    print(decrypted_message)
