from collections import deque


def make_christmas_presents(material_list: list[int], magic_list: list[int]) -> None:
    """
    This function mixes materials and magic values to craft presents for Christmas.

    Args:
        material_list (list[int]): List with material amounts.
        magic_list (list[int]): List with magic amounts.

    Returns:
        None
    """
    materials = material_list
    magic = deque(magic_list)
    crafted = {}
    gifts = {
        150: 'Doll',
        250: 'Wooden train',
        300: 'Teddy bear',
        400: 'Bicycle',
    }
    while materials and magic:
        if materials[-1] == 0 and magic[0] == 0:
            materials.pop()
            magic.popleft()
            continue
        if materials[-1] == 0:
            materials.pop()
            continue
        if magic[0] == 0:
            magic.popleft()
            continue
        current_material = materials[-1]
        current_magic = magic[0]
        product = current_material * current_magic
        if product in gifts:
            present = gifts[product]
            crafted[present] = crafted.get(present, 0) + 1
            materials.pop()
            magic.popleft()
        elif product < 0:
            materials.pop()
            magic.popleft()
            materials.append(current_material + current_magic)
        else:
            magic.popleft()
            materials[-1] += 15
    success = (crafted.get('Doll', 0) >= 1 and crafted.get('Wooden train', 0) >= 1) or (
            crafted.get('Teddy bear', 0) >= 1 and crafted.get('Bicycle', 0) >= 1)
    print('The presents are crafted! Merry Christmas!' if success else 'No presents this Christmas!')
    if materials:
        print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
    if magic:
        print(f"Magic left: {', '.join(str(x) for x in magic)}")
    for gift in sorted(crafted):
        print(f"{gift}: {crafted[gift]}")


if __name__ == '__main__':
    materials_input = [int(x) for x in input().split()]
    magic_input = [int(x) for x in input().split()]
    make_christmas_presents(material_list=materials_input, magic_list=magic_input)
