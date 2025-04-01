import re


def count_word_occurrences(text: str, word: str) -> int:
    """
    Counts occurrences of the given word in the text using a case-insensitive regex search.
    """
    pattern = rf'\b{re.escape(word)}\b'
    matches = re.findall(pattern, text, re.IGNORECASE)
    count = len(matches)
    return count


if __name__ == '__main__':
    input_text = input().strip()
    search_word = input().strip()

    result = count_word_occurrences(text=input_text, word=search_word)
    print(result)
