def print_ascii_range(start: int, end: int) -> str:
    return ' '.join(chr(i) for i in range(start, end + 1))


if __name__ == '__main__':
    start_index = int(input())
    end_index = int(input())
    result = print_ascii_range(start=start_index, end=end_index)
    print(result)
