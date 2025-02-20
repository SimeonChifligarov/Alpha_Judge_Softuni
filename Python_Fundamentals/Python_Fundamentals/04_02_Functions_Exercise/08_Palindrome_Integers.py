def check_if_word_is_palindrome(num):
    word = str(num)
    # if word == word[::-1]:
    #     return True
    # return False

    return word == word[::-1]


list_of_numbers = [int(el) for el in input().split(', ')]
for number in list_of_numbers:
    print(check_if_word_is_palindrome(number))
