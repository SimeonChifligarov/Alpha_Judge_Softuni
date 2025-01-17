def process_numbers(count):
    for _ in range(count):
        num = int(input())
        if num % 2 != 0:
            print(f'{num} is odd!')
            break
    else:
        print('All numbers are even.')


if __name__ == '__main__':
    n_input = int(input())
    process_numbers(count=n_input)
