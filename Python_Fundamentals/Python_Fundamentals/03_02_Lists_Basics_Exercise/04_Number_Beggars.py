# You will receive 2 lines of input: a single string containing the numbers separated by a comma
# and a space ', '. On the second line you will receive the number of beggars.

list_of_digits_from_string = [int(x) for x in input().split(', ')]
number_of_beggars = int(input())

money_for_each_beggar = []
for beggar in range(1, number_of_beggars + 1):
    beggar_sum = 0
    for offer in range(beggar, len(list_of_digits_from_string) + 1, number_of_beggars):
        beggar_sum += list_of_digits_from_string[offer - 1]
    money_for_each_beggar.append(beggar_sum)

print(money_for_each_beggar)
