def find_palindromes():
    """
    Reads a space-separated list of words from user input and searches for palindromes.
    Prints the list of found palindromes and the count of a specified searched palindrome.
    """
    words = input().split()
    searched_palindrome = input()

    palindromes = [word for word in words if word == word[::-1]]

    print(palindromes)
    print(f'Found palindrome {palindromes.count(searched_palindrome)} times')


if __name__ == "__main__":
    find_palindromes()
