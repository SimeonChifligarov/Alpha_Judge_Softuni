if __name__ == '__main__':
    numbers_input = input().split()
    rounded_numbers = [round(float(num)) for num in numbers_input]
    print(rounded_numbers)
