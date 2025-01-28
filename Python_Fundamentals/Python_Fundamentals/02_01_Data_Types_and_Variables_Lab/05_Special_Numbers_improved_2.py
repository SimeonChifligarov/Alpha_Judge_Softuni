number = int(input())

for num in range(1, number + 1):
    num_as_string = str(num)
    num_as_list = [int(digit) for digit in num_as_string]
    print(f'{num} -> {sum(num_as_list) in {5, 7, 11}}')
