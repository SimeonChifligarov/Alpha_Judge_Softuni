def sum_ascii_codes(count: int) -> str:
    total = 0
    for _ in range(count):
        char = input()
        total += ord(char)
    return f'The sum equals: {total}'


if __name__ == '__main__':
    num_chars = int(input())
    result = sum_ascii_codes(count=num_chars)
    print(result)
