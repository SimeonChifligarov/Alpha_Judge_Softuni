def palindrome(word: str, index: int) -> str:
    """
    This function checks if a word is a palindrome using recursion.

    Args:
        word: The word to check
        index: The current index (starts from 0)

    Returns:
        A string telling if the word is a palindrome or not
    """
    if index >= len(word) // 2:
        return f'{word} is a palindrome'
    if word[index] != word[-(index + 1)]:
        return f'{word} is not a palindrome'
    return palindrome(word=word, index=index + 1)

# if __name__ == '__main__':
#     given_word = input()
#     print(palindrome(word=given_word, index=0))
