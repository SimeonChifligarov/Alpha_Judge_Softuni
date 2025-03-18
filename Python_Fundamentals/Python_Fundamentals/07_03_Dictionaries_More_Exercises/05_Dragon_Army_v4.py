from collections import defaultdict


def process_dragons(n: int, dragon_data: list[str]) -> None:
    """
    Categorizes dragons by type, updates their stats, and prints the average stats per type
    """
    default_stats = {'damage': 45, 'health': 250, 'armor': 10}
    dragons = defaultdict(dict)

    for entry in dragon_data:
        type_, name, damage, health, armor = entry.split()

        damage = int(damage) if damage != 'null' else default_stats['damage']
        health = int(health) if health != 'null' else default_stats['health']
        armor = int(armor) if armor != 'null' else default_stats['armor']

        dragons[type_][name] = {'damage': damage, 'health': health, 'armor': armor}

    for type_ in dragons:
        sorted_dragons = dict(sorted(dragons[type_].items()))
        dragons[type_] = sorted_dragons

    for type_, dragon_list in dragons.items():
        avg_damage = sum(d['damage'] for d in dragon_list.values()) / len(dragon_list)
        avg_health = sum(d['health'] for d in dragon_list.values()) / len(dragon_list)
        avg_armor = sum(d['armor'] for d in dragon_list.values()) / len(dragon_list)

        print(f"{type_}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")

        for name, stats in dragon_list.items():
            print(f"-{name} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}")


if __name__ == '__main__':
    n_input = int(input())
    dragon_data_input = [input() for _ in range(n_input)]
    process_dragons(n=n_input, dragon_data=dragon_data_input)
