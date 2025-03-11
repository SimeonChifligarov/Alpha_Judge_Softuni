def collect_synonyms(n: int) -> dict:
    """Collects words and their synonyms into a dictionary."""
    synonyms = {}

    for _ in range(n):
        word = input()
        synonym = input()

        if word not in synonyms:
            synonyms[word] = []
        synonyms[word].append(synonym)

    return synonyms


def print_synonyms(synonyms: dict) -> None:
    """Prints the words and their synonyms in the required format."""
    for word, synonym_list in synonyms.items():
        print(f"{word} - {', '.join(synonym_list)}")


if __name__ == '__main__':
    words_count = int(input())
    synonyms_dict = collect_synonyms(n=words_count)
    print_synonyms(synonyms_dict)
