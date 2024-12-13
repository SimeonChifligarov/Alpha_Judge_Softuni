numbers_count = int(input())

numbers = [int(input()) for _ in range(numbers_count)]

average = sum(numbers) / len(numbers)
print(f'{average:.2f}')
