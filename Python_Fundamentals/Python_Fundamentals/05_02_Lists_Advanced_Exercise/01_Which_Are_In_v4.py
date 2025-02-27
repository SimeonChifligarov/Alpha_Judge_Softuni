first_string_list = input().split(', ')
second_string_list = input().split(', ')

repetition_list = []
for first_string in first_string_list:
    for second_string in second_string_list:
        if first_string in second_string:
            repetition_list.append(first_string)
            break

# print(sorted(repetition_list, key=first_string_list.index))
print(repetition_list)
