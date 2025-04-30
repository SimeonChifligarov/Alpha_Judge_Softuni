def operate(sign: str, *nums: int) -> float:
    """
    This function does math with many numbers using a given operator.

    Args:
        sign (str): The math symbol to use.
        *nums (int): The numbers to apply the operation on.

    Returns:
        float: The final result after doing the math.
    """
    if sign == '+':
        result = sum(nums)
    elif sign == '-':
        result = nums[0]
        for number in nums[1:]:
            result -= number
    elif sign == '*':
        result = 1
        for number in nums:
            result *= number
    elif sign == '/':
        result = nums[0]
        for number in nums[1:]:
            if number == 0:
                continue
            result /= number
    return result

# if __name__ == '__main__':
#     operator_input = input()
#     numbers_input = [int(x) for x in input().split()]
#     final_result = operate(sign=operator_input, *numbers_input)
#     print(final_result)
