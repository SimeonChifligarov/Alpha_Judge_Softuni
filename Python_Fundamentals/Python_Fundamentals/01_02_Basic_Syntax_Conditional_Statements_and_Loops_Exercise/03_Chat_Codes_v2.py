def process_messages(message_count):
    for _ in range(message_count):
        number = int(input())
        if number == 88:
            print('Hello')
        elif number == 86:
            print('How are you?')
        elif number < 88:
            print('GREAT!')
        else:
            print('Bye.')


if __name__ == '__main__':
    n_input = int(input())
    process_messages(message_count=n_input)
