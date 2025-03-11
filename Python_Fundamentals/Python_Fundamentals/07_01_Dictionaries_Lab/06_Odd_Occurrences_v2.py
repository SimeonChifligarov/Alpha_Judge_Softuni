def find_odd_occurrences(words: list[str]) -> list[str]:
    """Finds words that appear an odd number of times, case-insensitive."""
    word_counts = {}

    for word in words:
        word_lower = word.lower()
        word_counts[word_lower] = word_counts.get(word_lower, 0) + 1

    return [w for w in word_counts if word_counts[w] % 2 == 1]


if __name__ == '__main__':
    word_list = input().split()
    results = find_odd_occurrences(words=word_list)
    print(' '.join(dict.fromkeys(results)))
