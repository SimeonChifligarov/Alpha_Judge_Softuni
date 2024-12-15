def generate_special_numbers(start, end):
    special_numbers = []
    for d1 in range(start, end + 1):
        for d2 in range(start, end + 1):
            for d3 in range(start, end + 1):
                for d4 in range(start, end + 1):
                    # if (d1 % 2 == 0 and d4 % 2 != 0) or (d1 % 2 != 0 and d4 % 2 == 0):
                    #     if d1 > d4:
                    #         if (d2 + d3) % 2 == 0:
                    #             special_number = int(f'{d1}{d2}{d3}{d4}')
                    #             special_numbers.append(special_number)
                    if (
                            ((d1 % 2 == 0 and d4 % 2 != 0) or (d1 % 2 != 0 and d4 % 2 == 0))
                            and (d1 > d4)
                            and ((d2 + d3) % 2 == 0)
                    ):
                        special_number = int(f'{d1}{d2}{d3}{d4}')
                        special_numbers.append(special_number)

    return special_numbers


start_n = int(input())
end_n = int(input())

s_nums = generate_special_numbers(start_n, end_n)
# print(' '.join(map(str, s_nums)))
print(*s_nums)
