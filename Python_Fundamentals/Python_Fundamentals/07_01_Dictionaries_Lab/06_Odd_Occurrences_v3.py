def find_odd_occurrences(words: list[str]) -> list[str]:
    """Finds words that appear an odd number of times, case-insensitive."""
    word_counts = dict.fromkeys(words, 0)

    for word in words:
        word_counts[word] += 1

    return [w for w in word_counts if word_counts[w] % 2 == 1]


if __name__ == '__main__':
    word_list = input().lower().split()
    results = find_odd_occurrences(words=word_list)
    print(' '.join(results))
