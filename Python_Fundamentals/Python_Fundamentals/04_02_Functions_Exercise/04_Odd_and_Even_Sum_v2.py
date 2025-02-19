def sum_of_even_and_odd_digits(num):
    num_as_string = str(num)
    even_sum = 0
    odd_sum = 0
    for index in range(len(num_as_string)):
        if int(num_as_string[index]) % 2 == 0:
            even_sum += int(num_as_string[index])
        else:
            odd_sum += int(num_as_string[index])
    return print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')


number = int(input())
sum_of_even_and_odd_digits(number)
