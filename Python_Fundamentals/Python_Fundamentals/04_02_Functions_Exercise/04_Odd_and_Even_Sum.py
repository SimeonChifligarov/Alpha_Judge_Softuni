# You will receive a single number. You have to write a function that returns
# the sum of all even and all odd digits from that number as a single string
# like in the examples below.

def sum_of_even_and_odd_digits(num):
    num_as_string = str(num)
    even_sum = 0
    odd_sum = 0
    for char in num_as_string:
        if int(char) % 2 == 0:
            even_sum += int(char)
        else:
            odd_sum += int(char)
    return odd_sum, even_sum


number = int(input())
result = sum_of_even_and_odd_digits(number)
odd_sum_output, even_sum_output = result
print(f'Odd sum = {odd_sum_output}, Even sum = {even_sum_output}')
