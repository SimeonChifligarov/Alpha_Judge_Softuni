def process_names(names_count: int) -> set:
    """
    This function processes names, calculates ascii values, and decides the final set.

    Args:
        names_count (int): How many names will be processed

    Returns:
        set: A final set depending on sums comparison
    """
    odd_numbers = set()
    even_numbers = set()
    for line_number in range(1, names_count + 1):
        name_input = input()
        ascii_sum = sum(ord(char) for char in name_input)
        result_number = ascii_sum // line_number
        if result_number % 2 == 0:
            even_numbers.add(result_number)
        else:
            odd_numbers.add(result_number)
    odd_sum = sum(odd_numbers)
    even_sum = sum(even_numbers)
    if odd_sum == even_sum:
        return odd_numbers.union(even_numbers)
    if odd_sum > even_sum:
        return odd_numbers.difference(even_numbers)
    return odd_numbers.symmetric_difference(even_numbers)


if __name__ == '__main__':
    total_names = int(input())
    final_result = process_names(names_count=total_names)
    print(', '.join(str(num) for num in final_result))
