number = int(input())

is_valid_number = -100 <= number <= 100 and number != 0

print('Yes' if is_valid_number else 'No')
