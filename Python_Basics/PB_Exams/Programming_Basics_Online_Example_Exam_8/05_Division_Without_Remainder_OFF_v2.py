def calculate_percentages(numbers, total_count):
    divisible_by_2 = 0
    divisible_by_3 = 0
    divisible_by_4 = 0

    for number in numbers:
        if number % 2 == 0:
            divisible_by_2 += 1
        if number % 3 == 0:
            divisible_by_3 += 1
        if number % 4 == 0:
            divisible_by_4 += 1

    # print(f'{(divisible_by_2 / total_count):.2%}')
    # print(f'{(divisible_by_3 / total_count):.2%}')
    # print(f'{(divisible_by_4 / total_count):.2%}')

    percentage_by_2 = divisible_by_2 / total_count
    percentage_by_3 = divisible_by_3 / total_count
    percentage_by_4 = divisible_by_4 / total_count

    print(f'{percentage_by_2:.2%}')
    print(f'{percentage_by_3:.2%}')
    print(f'{percentage_by_4:.2%}')


if __name__ == '__main__':
    count_of_numbers = int(input())
    input_numbers = [int(input()) for _ in range(count_of_numbers)]
    calculate_percentages(numbers=input_numbers, total_count=count_of_numbers)
