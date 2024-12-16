def generate_combinations(one_lv_count, two_lv_count, five_lv_count, target_sum):
    for ones in range(0, one_lv_count + 1):
        for twos in range(0, two_lv_count + 1):
            for fives in range(0, five_lv_count + 1):
                total = ones * 1 + twos * 2 + fives * 5
                if total == target_sum:
                    yield f'{ones} * 1 lv. + {twos} * 2 lv. + {fives} * 5 lv. = {target_sum} lv.'


def find_combinations(one_lv_count, two_lv_count, five_lv_count, target_sum):
    for combination in generate_combinations(one_lv_count, two_lv_count, five_lv_count, target_sum):
        print(combination)


one_lv_c = int(input())
two_lv_c = int(input())
five_lv_c = int(input())
target_s = int(input())

find_combinations(one_lv_count=one_lv_c, two_lv_count=two_lv_c, five_lv_count=five_lv_c, target_sum=target_s)
