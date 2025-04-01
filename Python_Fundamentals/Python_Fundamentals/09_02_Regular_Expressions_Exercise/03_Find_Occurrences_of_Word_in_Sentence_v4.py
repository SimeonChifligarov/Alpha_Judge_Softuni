import re


def count_word_occurrences(text: str, word: str) -> int:
    """
    Counts occurrences of the given word in the text using a case-insensitive regex search.
    """
    return len(re.findall(rf'\b{re.escape(word)}\b', text, re.IGNORECASE))


if __name__ == '__main__':
    input_text = input().strip()
    search_word = input().strip()

    result = count_word_occurrences(text=input_text, word=search_word)
    print(result)
