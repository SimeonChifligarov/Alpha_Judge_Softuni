def find_number_in_range():
    while True:
        num = float(input())
        if 1 <= num <= 100:
            print(f'The number {num} is between 1 and 100')
            break


if __name__ == '__main__':
    find_number_in_range()
