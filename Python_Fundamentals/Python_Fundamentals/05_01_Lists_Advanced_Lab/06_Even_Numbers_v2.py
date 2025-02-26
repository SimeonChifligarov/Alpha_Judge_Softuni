# Convert the list of strings into a list of numbers
number_list = list(map(int, input().split(', ')))

# Find all the even numbers' indices
found_indices_or_no = map(
    lambda x: x if number_list[x] % 2 == 0 else 'no',
    range(len(number_list)))

# Filter only the indices
even_indices = list(filter(lambda a: a != 'no', found_indices_or_no))
print(even_indices)
