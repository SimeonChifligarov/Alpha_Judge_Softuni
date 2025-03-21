def character_multiplier(word_one: str, word_two: str) -> int:
    """Calculates the character multiplier sum of `word_one` and `word_two`."""
    min_len = min(len(word_one), len(word_two))
    total_result = sum(ord(word_one[i]) * ord(word_two[i]) for i in range(min_len))

    longer_word = word_one if len(word_one) > len(word_two) else word_two
    total_result += sum(ord(char) for char in longer_word[min_len:])

    return total_result


if __name__ == '__main__':
    word_one_input, word_two_input = input().split()

    result: int = character_multiplier(word_one_input, word_two_input)
    print(result)
