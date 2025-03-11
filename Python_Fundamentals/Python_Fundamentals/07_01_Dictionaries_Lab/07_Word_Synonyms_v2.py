def collect_synonyms(n: int) -> dict[str, list[str]]:
    """Collects synonyms for words from user input."""
    synonyms_dict = {}

    for _ in range(n):
        word = input()
        synonym = input()
        if word not in synonyms_dict:
            synonyms_dict[word] = []
        synonyms_dict[word].append(synonym)

    return synonyms_dict


def format_synonyms_output(synonyms: dict[str, list[str]]) -> str:
    """Formats the synonyms dictionary into the required output format."""
    return '\n'.join(f"{word} - {', '.join(syn_list)}" for word, syn_list in synonyms.items())


if __name__ == '__main__':
    count = int(input())
    synonyms_dictionary = collect_synonyms(n=count)
    print(format_synonyms_output(synonyms=synonyms_dictionary))
