def calc_sum(numbers, idx):
    if idx == len(numbers) - 1:
        return numbers[idx]

    return numbers[idx] + calc_sum(numbers, idx + 1)


if __name__ == '__main__':
    input_numbers = [int(el) for el in input().split()]
    total_sum = calc_sum(numbers=input_numbers, idx=0)
    print(total_sum)
