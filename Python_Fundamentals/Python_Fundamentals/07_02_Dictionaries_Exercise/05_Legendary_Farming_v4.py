def obtain_legendary_item() -> None:
    """
    Determines the first legendary item obtained based on material collection.
    Prints the obtained item, remaining key materials, and collected junk items.
    """
    required_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
    junk_items = {}

    legendary_items = {
        'shards': 'Shadowmourne',
        'fragments': 'Valanyr',
        'motes': 'Dragonwrath',
    }

    while True:
        inputs = [el.lower() if i % 2 else int(el) for i, el in enumerate(input().split())]

        for i in range(0, len(inputs), 2):
            quantity, material = inputs[i], inputs[i + 1]

            if material in required_materials:
                required_materials[material] += quantity
                if required_materials[material] >= 250:
                    print(f'{legendary_items[material]} obtained!')
                    required_materials[material] -= 250
                    print(f'shards: {required_materials["shards"]}')
                    print(f'fragments: {required_materials["fragments"]}')
                    print(f'motes: {required_materials["motes"]}')
                    for item, count in junk_items.items():
                        print(f'{item}: {count}')
                    return
            else:
                junk_items[material] = junk_items.get(material, 0) + quantity


if __name__ == '__main__':
    obtain_legendary_item()
