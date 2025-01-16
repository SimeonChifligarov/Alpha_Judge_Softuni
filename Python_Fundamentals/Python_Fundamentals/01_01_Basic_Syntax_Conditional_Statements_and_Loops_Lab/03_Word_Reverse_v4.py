def reverse_word(word):
    return word[::-1]


if __name__ == '__main__':
    user_input = input()
    reversed_result = reverse_word(word=user_input)
    print(reversed_result)
