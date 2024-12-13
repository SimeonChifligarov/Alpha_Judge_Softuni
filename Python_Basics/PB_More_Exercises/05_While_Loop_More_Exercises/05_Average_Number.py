numbers_count = int(input())
total_sum = 0
for _ in range(numbers_count):
    number = int(input())
    total_sum += number

average = total_sum / numbers_count
print(f'{average:.2f}')
