NO_STRING = 'No'

n = int(input())
numbers = [float(input()) for _ in range(n)]

odd_numbers = []
even_numbers = []

for i in range(n):
    current_number = numbers[i]

    if (i + 1) % 2 == 0:
        even_numbers.append(current_number)
    else:
        odd_numbers.append(current_number)

odd_sum = f'{sum(odd_numbers):.2f}'
odd_min = f'{min(odd_numbers):.2f}' if odd_numbers else NO_STRING
odd_max = f'{max(odd_numbers):.2f}' if odd_numbers else NO_STRING

even_sum = f'{sum(even_numbers):.2f}'
even_min = f'{min(even_numbers):.2f}' if even_numbers else NO_STRING
even_max = f'{max(even_numbers):.2f}' if even_numbers else NO_STRING

result = [
    f'OddSum={odd_sum}',
    f'OddMin={odd_min}',
    f'OddMax={odd_max}',
    f'EvenSum={even_sum}',
    f'EvenMin={even_min}',
    f'EvenMax={even_max}',
]

print(*result, sep=',\n')
