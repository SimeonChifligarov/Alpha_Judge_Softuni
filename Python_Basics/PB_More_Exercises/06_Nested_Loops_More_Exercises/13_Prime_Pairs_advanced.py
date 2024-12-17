def check_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def create_numbers(start_a, start_b, range_a, range_b):
    limit_a = start_a + range_a
    limit_b = start_b + range_b

    for value_a in range(start_a, limit_a + 1):
        if check_prime(value_a):
            for value_b in range(start_b, limit_b + 1):
                if check_prime(value_b):
                    print(f'{value_a}{value_b}')


first_start = int(input())
second_start = int(input())
first_range = int(input())
second_range = int(input())

create_numbers(start_a=first_start, start_b=second_start, range_a=first_range, range_b=second_range)
