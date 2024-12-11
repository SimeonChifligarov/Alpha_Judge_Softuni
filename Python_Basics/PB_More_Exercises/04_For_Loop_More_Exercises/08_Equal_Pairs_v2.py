n = int(input())

first_num, second_num = int(input()), int(input())
current_sum = first_num + second_num

diff_sum = 0

for _ in range(n - 1):
    num1, num2 = int(input()), int(input())
    next_sum = num1 + num2

    if abs(current_sum - next_sum) > diff_sum:
        diff_sum = abs(current_sum - next_sum)

    current_sum = next_sum

if diff_sum == 0:
    print(f'Yes, value={current_sum}')
else:
    print(f'No, maxdiff={diff_sum}')

