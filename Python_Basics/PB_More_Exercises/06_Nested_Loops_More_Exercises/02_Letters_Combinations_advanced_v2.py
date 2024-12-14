start_letter = input()
end_letter = input()
excluded_letter = input()

results = []
count_combinations = 0

for first_letter in range(ord(start_letter), ord(end_letter) + 1):
    for second_letter in range(ord(start_letter), ord(end_letter) + 1):
        for third_letter in range(ord(start_letter), ord(end_letter) + 1):
            if excluded_letter not in [chr(first_letter), chr(second_letter), chr(third_letter)]:
                results.append(f'{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}')
                count_combinations += 1

results.append(count_combinations)
print(*results, sep=' ')
