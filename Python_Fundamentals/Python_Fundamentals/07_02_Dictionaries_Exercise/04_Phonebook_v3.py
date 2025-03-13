def build_phonebook() -> tuple[dict[str, str], int]:
    """
    Builds a phonebook from user input where each entry is in the format 'name-number'.
    Updates existing contacts if the name already exists.
    """
    phonebook: dict[str, str] = {}

    while True:
        entry = input()
        if entry.isdigit():
            return phonebook, int(entry)

        name, number = entry.split('-')
        phonebook[name] = number


def search_contacts(phonebook: dict[str, str], queries: int) -> None:
    """
    Searches for contacts in the phonebook based on user input.
    """
    for _ in range(queries):
        name = input()
        if name in phonebook:
            print(f'{name} -> {phonebook[name]}')
        else:
            print(f'Contact {name} does not exist.')


if __name__ == '__main__':
    phonebook_data, query_count = build_phonebook()
    search_contacts(phonebook=phonebook_data, queries=query_count)
