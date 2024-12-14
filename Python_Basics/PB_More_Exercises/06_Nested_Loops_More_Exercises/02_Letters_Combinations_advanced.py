start_letter = input()
end_letter = input()
excluded_letter = input()

count_combinations = 0

for first_letter in range(ord(start_letter), ord(end_letter) + 1):
    for second_letter in range(ord(start_letter), ord(end_letter) + 1):
        for third_letter in range(ord(start_letter), ord(end_letter) + 1):
            if all(chr(letter) != excluded_letter for letter in [first_letter, second_letter, third_letter]):
                print(f'{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}', end=' ')
                count_combinations += 1

print(count_combinations)
