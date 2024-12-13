def decode_hidden_message():
    secret_command = {'c', 'o', 'n'}
    encountered = set()
    current_word = []
    result = []

    while True:
        char = input()

        if char == 'End':
            break

        if not char.isalpha():
            continue

        if char in secret_command:
            if char not in encountered:
                encountered.add(char)
            else:
                current_word.append(char)
        else:
            current_word.append(char)

        if encountered == secret_command:
            result.append(''.join(current_word))
            current_word = []
            encountered.clear()

    print(' '.join(result))


decode_hidden_message()
