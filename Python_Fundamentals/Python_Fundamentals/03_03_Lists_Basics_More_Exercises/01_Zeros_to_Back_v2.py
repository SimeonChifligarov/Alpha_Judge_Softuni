from typing import List


def move_zeros_to_back(numbers: List[int]) -> List[int]:
    """
    Moves all zeros in the input list to the back, preserving the order of other elements.
    """

    non_zero = [num for num in numbers if num != 0]
    zeros = [0] * (len(numbers) - len(non_zero))

    return non_zero + zeros


if __name__ == '__main__':
    input_data = input()
    input_list = list(map(int, input_data.split(', ')))
    result = move_zeros_to_back(numbers=input_list)
    print(result)
