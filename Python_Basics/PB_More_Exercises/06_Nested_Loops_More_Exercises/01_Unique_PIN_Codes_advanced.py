upper_limit_first_digit = int(input())
upper_limit_second_digit = int(input())
upper_limit_third_digit = int(input())

prime_numbers = {2, 3, 5, 7}

for first_digit in range(2, upper_limit_first_digit + 1, 2):
    for second_digit in range(2, upper_limit_second_digit + 1):
        if second_digit in prime_numbers:
            for third_digit in range(2, upper_limit_third_digit + 1, 2):
                print(f'{first_digit} {second_digit} {third_digit}')
