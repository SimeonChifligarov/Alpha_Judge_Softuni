def find_largest_number_from_digits(number):
    digits = sorted(str(number), reverse=True)
    largest_number = int(''.join(digits))
    return largest_number


if __name__ == '__main__':
    input_number = int(input())
    result = find_largest_number_from_digits(number=input_number)
    print(result)
