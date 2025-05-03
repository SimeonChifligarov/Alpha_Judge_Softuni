def palindrome(word_input: str, idx: int) -> str:
    """
    This function checks if a word reads the same from both sides using recursion.

    Args:
        word_input: The word we want to check
        idx: The current index to compare letters

    Returns:
        A message if the word is a palindrome or not
    """
    reversed_idx = len(word_input) - idx - 1
    if idx >= reversed_idx:
        return f'{word_input} is a palindrome'
    if word_input[idx] != word_input[reversed_idx]:
        return f'{word_input} is not a palindrome'
    return palindrome(word_input=word_input, idx=idx + 1)

# if __name__ == '__main__':
#     input_word = input()
#     print(palindrome(word_input=input_word, idx=0))
