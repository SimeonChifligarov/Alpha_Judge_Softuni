first_string_list = input().split(', ')
second_string_list = input().split(', ')

repetition_list = []
for i in range(len(first_string_list)):
    for j in range(len(second_string_list)):
        if first_string_list[i] in second_string_list[j]:
            repetition_list.append(first_string_list[i])

print(sorted(set(repetition_list), key=first_string_list.index))
