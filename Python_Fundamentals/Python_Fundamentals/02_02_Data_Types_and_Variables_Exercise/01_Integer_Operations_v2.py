def calculate_expression(num1: int, num2: int, num3: int, num4: int) -> int:
    return ((num1 + num2) // num3) * num4


if __name__ == '__main__':
    first_input = int(input())
    second_input = int(input())
    third_input = int(input())
    fourth_input = int(input())
    output = calculate_expression(num1=first_input, num2=second_input, num3=third_input, num4=fourth_input)
    print(output)
