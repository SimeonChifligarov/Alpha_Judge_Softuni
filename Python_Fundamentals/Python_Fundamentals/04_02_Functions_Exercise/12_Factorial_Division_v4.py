import math

if __name__ == '__main__':
    # num_1, num_2 = int(input()), int(input())
    num_1 = int(input())
    num_2 = int(input())
    result = math.factorial(num_1) / math.factorial(num_2)
    print(f'{result:.2f}')
