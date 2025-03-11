def find_odd_occurrences(words: str) -> list:
    """Finds words that appear an odd number of times, case-insensitively."""
    word_list = words.lower().split()
    word_count = {word: word_list.count(word) for word in set(word_list)}

    return [w for w in word_list if word_count[w] % 2 != 0]


if __name__ == '__main__':
    words_input = input()
    odd_occurrence_words = find_odd_occurrences(words_input)

    print(' '.join(dict.fromkeys(odd_occurrence_words)))
