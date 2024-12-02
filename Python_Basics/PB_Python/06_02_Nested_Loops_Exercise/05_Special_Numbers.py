n = int(input())

special_numbers = []

for num in range(1111, 10000):
    digits = [int(digit) for digit in str(num)]
    if all(digit != 0 and n % digit == 0 for digit in digits):
        special_numbers.append(str(num))

print(' '.join(special_numbers))
