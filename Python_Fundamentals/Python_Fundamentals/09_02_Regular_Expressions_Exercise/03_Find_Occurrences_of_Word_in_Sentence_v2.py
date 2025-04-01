import re


def count_word_occurrences(text: str, target_word: str) -> int:
    """Counts occurrences of the exact `target_word` in `text`, case-insensitive."""

    pattern = fr'\b{re.escape(target_word)}\b'
    return len(re.findall(pattern, text, re.IGNORECASE))


if __name__ == '__main__':
    text_input: str = input().strip()
    target_word_input: str = input().strip()

    word_count: int = count_word_occurrences(text_input, target_word_input)
    print(word_count)
