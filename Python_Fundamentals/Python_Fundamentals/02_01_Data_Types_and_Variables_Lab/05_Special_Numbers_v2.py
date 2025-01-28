def is_special_number(num):
    digit_sum = sum(int(digit) for digit in str(num))
    return digit_sum in {5, 7, 11}


if __name__ == '__main__':
    range_end = int(input())
    for current_number in range(1, range_end + 1):
        special_status = is_special_number(num=current_number)
        print(f'{current_number} -> {special_status}')
