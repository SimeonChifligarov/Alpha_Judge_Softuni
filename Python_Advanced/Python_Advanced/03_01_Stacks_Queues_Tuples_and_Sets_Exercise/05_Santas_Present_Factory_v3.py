from collections import deque


def christmas_factory(material_boxes: list[int], magic_levels: list[int]) -> None:
    """
    This function mixes materials and magic to create Christmas presents.

    Args:
        material_boxes (list[int]): List with material quantities.
        magic_levels (list[int]): List with magic values.

    Returns:
        None
    """
    materials = material_boxes
    magic = deque(magic_levels)
    presents = {}
    recipes = {
        150: 'Doll',
        250: 'Wooden train',
        300: 'Teddy bear',
        400: 'Bicycle',
    }
    while materials and magic:
        while materials and materials[-1] == 0:
            materials.pop()
        while magic and magic[0] == 0:
            magic.popleft()
        if not materials or not magic:
            break
        mat = materials[-1]
        mag = magic[0]
        outcome = mat * mag
        if outcome in recipes:
            toy = recipes[outcome]
            presents[toy] = presents.get(toy, 0) + 1
            materials.pop()
            magic.popleft()
        elif outcome < 0:
            materials.pop()
            magic.popleft()
            materials.append(mat + mag)
        else:
            magic.popleft()
            materials[-1] += 15
    crafted_success = ('Doll' in presents and 'Wooden train' in presents) or (
            'Teddy bear' in presents and 'Bicycle' in presents)
    print('The presents are crafted! Merry Christmas!' if crafted_success else 'No presents this Christmas!')
    if materials:
        print(f"Materials left: {', '.join(str(num) for num in reversed(materials))}")
    if magic:
        print(f"Magic left: {', '.join(str(num) for num in magic)}")
    for present_name in sorted(presents):
        print(f"{present_name}: {presents[present_name]}")


if __name__ == '__main__':
    materials_input = [int(el) for el in input().split()]
    magic_input = [int(el) for el in input().split()]
    christmas_factory(material_boxes=materials_input, magic_levels=magic_input)
