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


def search_contacts(phonebook: dict[str, str], queries: int) -> list[str]:
    """
    Searches for contacts in the phonebook based on user input and returns search results.
    """
    results = []
    for _ in range(queries):
        name = input()
        if name in phonebook:
            results.append(f'{name} -> {phonebook[name]}')
        else:
            results.append(f'Contact {name} does not exist.')
    return results


def print_results(results: list[str]) -> None:
    """
    Prints the search results.
    """
    for result in results:
        print(result)


if __name__ == '__main__':
    phonebook_data, query_count = build_phonebook()
    search_results = search_contacts(phonebook=phonebook_data, queries=query_count)
    print_results(results=search_results)
