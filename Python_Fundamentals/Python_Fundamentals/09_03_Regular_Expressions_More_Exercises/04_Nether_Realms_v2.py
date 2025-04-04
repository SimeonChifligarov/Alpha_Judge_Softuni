import re


def calculate_health(demon: str) -> int:
    """Calculates the health of a demon based on non-numeric characters."""
    health_chars = re.findall(r'[^0-9+\-*/.]', demon)
    return sum(ord(char) for char in health_chars)


def calculate_damage(demon: str) -> float:
    """Calculates the base damage of a demon and applies multipliers (* and /)."""
    damage_numbers = re.findall(r'-?\d+\.?\d*', demon)
    damage = sum(float(num) for num in damage_numbers) if damage_numbers else 0

    for char in demon:
        if char == '*':
            damage *= 2
        elif char == '/':
            damage /= 2

    return damage


def process_demons(demon_list: list[str]) -> list[tuple[str, int, float]]:
    """Processes a list of demon names and returns their sorted attributes."""
    demons = [(demon.strip(), calculate_health(demon.strip()), calculate_damage(demon.strip())) for demon in demon_list]
    return sorted(demons, key=lambda x: x[0])


def main():
    """Handles input and output."""
    all_demons = input().split(',')
    sorted_demons = process_demons(all_demons)

    for name, health, damage in sorted_demons:
        print(f'{name} - {health} health, {damage:.2f} damage')


if __name__ == '__main__':
    main()
