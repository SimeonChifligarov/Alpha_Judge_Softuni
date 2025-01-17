def process_numbers(numbers):
    for number in numbers:
        if number % 2 != 0:
            print(f'{number} is odd!')
            return
    print('All numbers are even.')


if __name__ == '__main__':
    n_input = int(input())
    # this solution works only with n_input inputs;
    # if they are less - due to 'If the program receives an odd number, print "{num} is odd!" and *end the program*.'
    # it will raise EOFError: EOF when reading a line
    num_list = [int(input()) for _ in range(n_input)]
    process_numbers(numbers=num_list)
