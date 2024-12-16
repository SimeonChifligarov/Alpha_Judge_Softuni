def find_magic_combination(start, end, magic_number):
    combination_count = 0
    for first in range(start, end + 1):
        for second in range(start, end + 1):
            combination_count += 1
            if first + second == magic_number:
                return f'Combination N:{combination_count} ({first} + {second} = {magic_number})'

    return f'{combination_count} combinations - neither equals {magic_number}'


start1 = int(input())
end1 = int(input())
magic_number1 = int(input())

result = find_magic_combination(start=start1, end=end1, magic_number=magic_number1)
print(result)
