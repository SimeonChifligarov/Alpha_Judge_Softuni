numbers_as_list = [int(num) for num in input().split(', ')]

group_of_tens_count = max(numbers_as_list) // 10
current_group_of_tens = 1
current_numbers_as_list = numbers_as_list
current_group_list = []

for current_group_of_tens in range(1, group_of_tens_count + 1):
    for number in current_numbers_as_list:
        if number <= current_group_of_tens * 10:
            current_group_list.append(number)
    print(f'Group of {current_group_of_tens * 10}\'s: {current_group_list}')
    current_numbers_as_list = [num for num in current_numbers_as_list if num not in current_group_list]
    current_group_list = []

if current_numbers_as_list:
    print(f'Group of {(group_of_tens_count + 1) * 10}\'s: {current_numbers_as_list}')
