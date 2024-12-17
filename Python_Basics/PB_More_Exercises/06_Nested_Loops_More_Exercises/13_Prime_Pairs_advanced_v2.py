def is_prime(value):
    if value < 2:
        return False
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return False
    return True


def generate_prime_pairs(start_x, start_y, range_x, range_y):
    end_x = start_x + range_x
    end_y = start_y + range_y

    for x in range(start_x, end_x + 1):
        if is_prime(x):
            for y in range(start_y, end_y + 1):
                if is_prime(y):
                    yield f'{x}{y}'


start1 = int(input())
start2 = int(input())
diff1 = int(input())
diff2 = int(input())

for result in generate_prime_pairs(start1, start2, diff1, diff2):
    print(result)
