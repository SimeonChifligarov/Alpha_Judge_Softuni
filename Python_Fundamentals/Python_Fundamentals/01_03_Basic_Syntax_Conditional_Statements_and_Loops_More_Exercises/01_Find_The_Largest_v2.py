number_as_string = input()

number_list = []
for i in range(len(number_as_string)):
    number_list.append(int(number_as_string[i]))
number_list.sort(reverse=True)

print(*number_list, sep='')
