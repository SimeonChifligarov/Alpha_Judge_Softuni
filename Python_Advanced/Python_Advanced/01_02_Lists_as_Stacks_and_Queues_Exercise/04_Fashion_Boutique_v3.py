def count_needed_racks(pile_of_clothes: list[int], single_rack_capacity: int) -> int:
    """
    This function finds out how many racks are needed
    to place all the clothes without going over the rack capacity.

    Args:
        pile_of_clothes: A list of numbers showing the clothes.
        single_rack_capacity: A number showing the space of one rack.

    Returns:
        A number showing how many racks were used.
    """
    total_racks = 0
    current_capacity = single_rack_capacity
    for piece in reversed(pile_of_clothes):
        if piece <= current_capacity:
            current_capacity -= piece
        else:
            total_racks += 1
            current_capacity = single_rack_capacity - piece
    total_racks += 1
    return total_racks


if __name__ == '__main__':
    clothes_stack = [int(el) for el in input().split()]
    rack_size = int(input())
    racks_result = count_needed_racks(pile_of_clothes=clothes_stack, single_rack_capacity=rack_size)
    print(racks_result)
