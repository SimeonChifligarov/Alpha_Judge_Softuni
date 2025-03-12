from collections import Counter


def count_characters(s: str) -> None:
    char_counts = Counter(s.replace(' ', ''))

    for char, count in char_counts.items():
        print(f'{char} -> {count}')


if __name__ == '__main__':
    input_string = input()
    count_characters(input_string)
