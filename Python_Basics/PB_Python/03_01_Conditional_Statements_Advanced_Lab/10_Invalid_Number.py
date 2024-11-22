number = int(input())

is_number_valid = (100 <= number <= 200) or number == 0

if not is_number_valid:
    print('invalid')
