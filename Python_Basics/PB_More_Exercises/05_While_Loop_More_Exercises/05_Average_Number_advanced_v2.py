numbers_count = int(input())

numbers = (int(input()) for _ in range(numbers_count))

total_sum = sum(numbers)
average = total_sum / numbers_count
print(f'{average:.2f}')
