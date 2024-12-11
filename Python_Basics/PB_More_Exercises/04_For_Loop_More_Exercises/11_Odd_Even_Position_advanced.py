NO_STRING = 'No'

n = int(input())
numbers = [float(input()) for _ in range(n)]

odd_sum = 0
even_sum = 0
odd_numbers = []
even_numbers = []

for i in range(n):
    current_number = numbers[i]

    if (i + 1) % 2 == 0:
        even_sum += current_number
        even_numbers.append(current_number)
    else:
        odd_sum += current_number
        odd_numbers.append(current_number)

odd_min = f'{min(odd_numbers):.2f}' if odd_numbers else NO_STRING
odd_max = f'{max(odd_numbers):.2f}' if odd_numbers else NO_STRING

even_min = f'{min(even_numbers):.2f}' if even_numbers else NO_STRING
even_max = f'{max(even_numbers):.2f}' if even_numbers else NO_STRING

print(f'OddSum={odd_sum:.2f},')
print(f'OddMin={odd_min},')
print(f'OddMax={odd_max},')
print(f'EvenSum={even_sum:.2f},')
print(f'EvenMin={even_min},')
print(f'EvenMax={even_max}')
