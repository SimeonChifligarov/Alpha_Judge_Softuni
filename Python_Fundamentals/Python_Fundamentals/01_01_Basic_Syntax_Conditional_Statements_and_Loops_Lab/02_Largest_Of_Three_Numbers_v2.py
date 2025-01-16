def find_largest_number(a, b, c):
    return max(a, b, c)


if __name__ == '__main__':
    first_num = int(input())
    second_num = int(input())
    third_num = int(input())
    largest = find_largest_number(a=first_num, b=second_num, c=third_num)
    print(largest)
