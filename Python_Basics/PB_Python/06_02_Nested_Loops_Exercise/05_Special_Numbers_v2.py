def is_special_number(dividend, number):
    digits = [int(digit) for digit in str(number)]
    return all(digit != 0 and dividend % digit == 0 for digit in digits)


n = int(input())
special_numbers = []

for number in range(1111, 10000):
    if is_special_number(n, number):
        special_numbers.append(str(number))

print(' '.join(special_numbers))
