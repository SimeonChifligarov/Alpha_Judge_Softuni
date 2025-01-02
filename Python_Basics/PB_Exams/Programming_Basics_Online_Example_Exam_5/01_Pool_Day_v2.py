import math


def calculate_pool_expenses(people_count, entry_fee, sunbed_price, umbrella_price):
    total_entry = people_count * entry_fee
    total_umbrellas = math.ceil(people_count / 2) * umbrella_price
    total_sunbeds = math.ceil(people_count * 0.75) * sunbed_price
    total_cost = total_entry + total_umbrellas + total_sunbeds
    print(f'{total_cost:.2f} lv.')


people = int(input())
entry = float(input())
sunbed = float(input())
umbrella = float(input())
calculate_pool_expenses(people, entry, sunbed, umbrella)
