def process_dragons():
    n = int(input())
    dragons = {}

    DEFAULT_DAMAGE = 45
    DEFAULT_HEALTH = 250
    DEFAULT_ARMOR = 10

    for _ in range(n):
        dragon_data = input().split()
        dragon_type, name = dragon_data[0], dragon_data[1]

        damage = int(dragon_data[2]) if dragon_data[2] != 'null' else DEFAULT_DAMAGE
        health = int(dragon_data[3]) if dragon_data[3] != 'null' else DEFAULT_HEALTH
        armor = int(dragon_data[4]) if dragon_data[4] != 'null' else DEFAULT_ARMOR

        if dragon_type not in dragons:
            dragons[dragon_type] = {}
        dragons[dragon_type][name] = (damage, health, armor)

    for dragon_type, dragon_list in dragons.items():
        avg_damage = sum(d[0] for d in dragon_list.values()) / len(dragon_list)
        avg_health = sum(d[1] for d in dragon_list.values()) / len(dragon_list)
        avg_armor = sum(d[2] for d in dragon_list.values()) / len(dragon_list)

        print(f'{dragon_type}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})')

        for name, (damage, health, armor) in sorted(dragon_list.items()):
            print(f'-{name} -> damage: {damage}, health: {health}, armor: {armor}')


if __name__ == '__main__':
    process_dragons()
