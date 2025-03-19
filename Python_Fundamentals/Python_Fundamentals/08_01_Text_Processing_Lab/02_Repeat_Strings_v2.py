def repeat_words():
    words = input().split()
    repeated_words = [word * len(word) for word in words]
    print(''.join(repeated_words))


if __name__ == '__main__':
    repeat_words()
