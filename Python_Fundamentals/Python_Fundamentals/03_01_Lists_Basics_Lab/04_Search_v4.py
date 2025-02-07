# You will receive a number n and a word. On the next n lines you will be given some strings.
# You have to add them in a list and print them. After that you have to filter out only the strings
# that include the given word and print that list too.

from typing import List


def filter_strings(count: int, keyword: str) -> List[List[str]]:
    all_strings = [input() for _ in range(count)]
    filtered_strings = [string for string in all_strings if keyword in string]
    return [all_strings, filtered_strings]


if __name__ == '__main__':
    count_input = int(input())
    keyword_input = input()
    all_strings_output, filtered_strings_output = filter_strings(count=count_input, keyword=keyword_input)
    print(all_strings_output)
    print(filtered_strings_output)
