result = []

first_num, second_num = int(input()), int(input())

f_n_as_str = str(first_num)
# f_f_digit, f_s_digit, f_t_digit, f_fo_digit = int(f_n_as_str[0]), int(f_n_as_str[1]), int(f_n_as_str[2]), int(
#     f_n_as_str[3])
f_f_digit, f_s_digit, f_t_digit, f_fo_digit = map(int, f_n_as_str)

s_n_as_str = str(second_num)
# s_f_digit, s_s_digit, s_t_digit, s_fo_digit = int(s_n_as_str[0]), int(s_n_as_str[1]), int(s_n_as_str[2]), int(
#     s_n_as_str[3])
s_f_digit, s_s_digit, s_t_digit, s_fo_digit = map(int, s_n_as_str)

for f_digit in range(f_f_digit, s_f_digit + 1):
    if f_digit % 2 == 0:
        continue
    for s_digit in range(f_s_digit, s_s_digit + 1):
        if s_digit % 2 == 0:
            continue
        for t_digit in range(f_t_digit, s_t_digit + 1):
            if t_digit % 2 == 0:
                continue
            for fo_digit in range(f_fo_digit, s_fo_digit + 1):
                if fo_digit % 2 == 0:
                    continue
                result.append(f'{f_digit}{s_digit}{t_digit}{fo_digit}')

print(*result, sep=' ')
