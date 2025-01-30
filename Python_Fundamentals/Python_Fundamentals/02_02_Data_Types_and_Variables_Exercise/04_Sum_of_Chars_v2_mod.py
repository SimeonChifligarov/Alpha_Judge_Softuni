def sum_ascii_codes(count: int) -> int:
    total = 0
    for _ in range(count):
        char = input()
        total += ord(char)
    return total


if __name__ == '__main__':
    num_chars = int(input())
    result = sum_ascii_codes(count=num_chars)
    print(f'The sum equals: {result}')
