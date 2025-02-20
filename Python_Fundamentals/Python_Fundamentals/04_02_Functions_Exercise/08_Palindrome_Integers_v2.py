def check_if_word_is_palindrome(word):
    # if word == word[::-1]:
    #     return True
    # return False

    return word == word[::-1]


list_of_numbers = input().split(', ')
for number_as_string in list_of_numbers:
    print(check_if_word_is_palindrome(number_as_string))
