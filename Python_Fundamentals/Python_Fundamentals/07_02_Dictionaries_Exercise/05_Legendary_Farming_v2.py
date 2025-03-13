def get_legendary_item():
    import sys
    from collections import defaultdict

    LEGENDARY_ITEMS = {
        'shards': 'Shadowmourne',
        'fragments': 'Valanyr',
        'motes': 'Dragonwrath',
    }

    key_materials = defaultdict(int)
    junk_items = defaultdict(int)

    for line in sys.stdin:
        materials = line.strip().split()

        for i in range(0, len(materials), 2):
            quantity = int(materials[i])
            material = materials[i + 1].lower()

            if material in LEGENDARY_ITEMS:
                key_materials[material] += quantity
                if key_materials[material] >= 250:
                    key_materials[material] -= 250
                    print(f'{LEGENDARY_ITEMS[material]} obtained!')
                    print_materials(key_materials, junk_items)
                    return
            else:
                junk_items[material] += quantity


def print_materials(key_materials, junk_items):
    for material in ['shards', 'fragments', 'motes']:
        print(f'{material}: {key_materials[material]}')

    for material, quantity in junk_items.items():
        print(f'{material}: {quantity}')


if __name__ == '__main__':
    get_legendary_item()
