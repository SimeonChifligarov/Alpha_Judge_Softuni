def generate_passwords(max_digit, max_letter_index):
    ord_a = 97
    for first_digit in range(1, max_digit + 1):
        for second_digit in range(1, max_digit + 1):
            for first_letter in range(max_letter_index):
                for second_letter in range(max_letter_index):
                    for last_digit in range(1, max_digit + 1):
                        if last_digit > first_digit and last_digit > second_digit:
                            password = (
                                f'{first_digit}{second_digit}'
                                f'{chr(ord_a + first_letter)}{chr(ord_a + second_letter)}{last_digit}'
                            )
                            yield password


n = int(input())
l = int(input())

print(' '.join(generate_passwords(n, l)))
