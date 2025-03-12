data = input()
data_without_spaces = [char for char in data if not char == ' ']

occurrences_dict = {}
for char in data_without_spaces:
    if char not in occurrences_dict:
        occurrences_dict[char] = 0
    occurrences_dict[char] += 1

for occur, count in occurrences_dict.items():
    print(f'{occur} -> {count}')
