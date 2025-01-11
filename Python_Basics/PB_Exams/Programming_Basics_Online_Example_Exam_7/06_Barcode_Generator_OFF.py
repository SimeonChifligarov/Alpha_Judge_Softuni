# BAD PROBLEM DESCRIPTION!
# does not give 100/100 in automatic system

result = []

starting_num = int(input())
ending_num = int(input())

for num in range(starting_num, ending_num + 1):
    num_as_str = str(num)
    first_digit = int(num_as_str[0])
    second_digit = int(num_as_str[1])
    third_digit = int(num_as_str[2])
    forth_digit = int(num_as_str[3])
    if first_digit % 2 != 0 and second_digit % 2 != 0 and third_digit % 2 != 0 and forth_digit % 2 != 0:
        result.append(num)

print(*result, sep=' ')
