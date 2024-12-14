def generate_lucky_numbers(N):
    lucky_numbers = []
    for d1 in range(1, 10):
        for d2 in range(1, 10):
            for d3 in range(1, 10):
                for d4 in range(1, 10):
                    sum_first_two = d1 + d2
                    sum_last_two = d3 + d4
                    
                    if sum_first_two == sum_last_two:
                        if N % sum_first_two == 0:
                            lucky_number = int(f'{d1}{d2}{d3}{d4}')
                            lucky_numbers.append(lucky_number)

    return lucky_numbers


N = int(input())

l_nums = generate_lucky_numbers(N)
# print(' '.join(map(str, l_nums)))
print(*l_nums)
