first_string_as_list = list(input())
second_string_as_list = list(input())

for index in range(len(first_string_as_list)):
    if first_string_as_list[index] == second_string_as_list[index]:
        continue
    else:
        first_string_as_list[index] = second_string_as_list[index]
        print(''.join(first_string_as_list))
