def phonebook_manager():
    phonebook = {}

    while True:
        entry = input().strip()
        if entry.isdigit():
            n = int(entry)
            break
        name, number = entry.split('-')
        phonebook[name] = number

    for _ in range(n):
        search_name = input().strip()
        if search_name in phonebook:
            print(f'{search_name} -> {phonebook[search_name]}')
        else:
            print(f'Contact {search_name} does not exist.')


if __name__ == '__main__':
    phonebook_manager()
