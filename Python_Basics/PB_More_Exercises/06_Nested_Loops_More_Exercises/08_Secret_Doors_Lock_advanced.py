def generate_combinations(hundreds_limit, tens_limit, units_limit):
    prime_numbers = [2, 3, 5, 7]
    combinations = []

    for hundreds in range(2, hundreds_limit + 1, 2):
        for tens in range(2, tens_limit + 1):
            if tens not in prime_numbers:
                continue
            for units in range(2, units_limit + 1, 2):
                combinations.append(f'{hundreds} {tens} {units}')

    return combinations


hundreds_l = int(input())
tens_l = int(input())
units_l = int(input())

gen_comb = generate_combinations(hundreds_limit=hundreds_l, tens_limit=tens_l, units_limit=units_l)
print('\n'.join(gen_comb))
