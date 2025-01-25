number = input()

number_as_list = [int(digit) for digit in number]
number_as_list.sort(reverse=True)
print(*number_as_list, sep='')
