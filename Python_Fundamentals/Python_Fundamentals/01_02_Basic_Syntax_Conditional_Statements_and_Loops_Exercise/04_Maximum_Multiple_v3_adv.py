def find_largest_divisible(num, limit):
    result = limit - (limit % num)
    return result


if __name__ == '__main__':
    divisor_input = int(input())
    boundary_input = int(input())
    largest_number = find_largest_divisible(num=divisor_input, limit=boundary_input)
    print(largest_number)
