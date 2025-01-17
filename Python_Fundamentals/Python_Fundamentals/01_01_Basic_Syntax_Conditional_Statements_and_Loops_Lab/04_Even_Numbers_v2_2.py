def process_numbers(count):
    for _ in range(count):
        num = int(input())
        if num % 2 != 0:
            return f'{num} is odd!'
    else:
        return 'All numbers are even.'


if __name__ == '__main__':
    n_input = int(input())
    result = process_numbers(count=n_input)
    print(result)
