def find_palindromes(words: list[str], target_palindrome: str) -> tuple[list[str], int]:
    """
    Finds all palindromes in the given list of words and counts occurrences of the target palindrome.
    """
    palindromes = [word for word in words if word == word[::-1]]
    palindrome_count = palindromes.count(target_palindrome)

    return palindromes, palindrome_count


if __name__ == '__main__':
    words_input = input().split()
    target_palindrome_input = input()
    found_palindromes, count = find_palindromes(words=words_input, target_palindrome=target_palindrome_input)

    print(found_palindromes)
    print(f'Found palindrome {count} times')
