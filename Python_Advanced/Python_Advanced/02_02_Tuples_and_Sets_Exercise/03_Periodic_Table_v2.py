def collect_chemical_elements(lines_count: int) -> set:
    """
    This function collects all unique chemical elements.

    Args:
        lines_count (int): Number of input lines

    Returns:
        set: A set with all different chemical elements
    """
    chemical_elements = set()
    for _ in range(lines_count):
        elements_list = input().split()
        chemical_elements.update(elements_list)
    return chemical_elements


if __name__ == '__main__':
    input_lines = int(input())
    unique_chemicals = collect_chemical_elements(lines_count=input_lines)
    for chemical in unique_chemicals:
        print(chemical)
