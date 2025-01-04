import math


def find_most_powerful_word():
    vowels = {'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'}
    most_powerful_word = ''
    max_power = 0

    while True:
        word = input()
        if word == 'End of words':
            break

        ascii_sum = sum(ord(char) for char in word)
        word_length = len(word)

        if word[0] in vowels:
            power = ascii_sum * word_length
        else:
            power = math.floor(ascii_sum / word_length)

        if power > max_power:
            max_power = power
            most_powerful_word = word

    print(f'The most powerful word is {most_powerful_word} - {max_power}')


if __name__ == '__main__':
    find_most_powerful_word()
