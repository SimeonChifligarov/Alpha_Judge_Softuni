def calculate_racks_needed(clothes_list: list[int], rack_capacity: int) -> int:
    """
    This function calculates how many racks are needed
    to hang all the clothes based on the rack capacity.

    Args:
        clothes_list: A list of integers representing the clothes.
        rack_capacity: An integer showing the capacity of one rack.

    Returns:
        An integer with the number of racks needed.
    """
    racks_used = 1
    current_load = 0
    while clothes_list:
        current_piece = clothes_list.pop()
        if current_load + current_piece <= rack_capacity:
            current_load += current_piece
        else:
            racks_used += 1
            current_load = current_piece
    return racks_used


if __name__ == '__main__':
    clothes_input = [int(el) for el in input().split()]
    rack_capacity_input = int(input())
    result = calculate_racks_needed(clothes_list=clothes_input, rack_capacity=rack_capacity_input)
    print(result)
