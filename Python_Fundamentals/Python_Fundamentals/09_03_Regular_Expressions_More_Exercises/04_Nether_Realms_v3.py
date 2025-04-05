import re


def calculate_demon_health(demon_name: str) -> int:
    """
    Calculates the health of a demon by summing the ASCII values of all non-numeric,
    non-arithmetic, and non-delimiter characters.
    """
    health_chars = re.findall(r'[^0-9+\-*/.]', demon_name)
    return sum(ord(char) for char in health_chars)


def calculate_demon_damage(demon_name: str) -> float:
    """
    Calculates the base damage of a demon by summing all numbers in its name,
    then applying multiplication and division operations in order of appearance.
    """
    base_damage_numbers = re.findall(r'[-+]?\d+\.?\d*', demon_name)
    base_damage = sum(float(num) for num in base_damage_numbers)

    for symbol in demon_name:
        if symbol == '*':
            base_damage *= 2
        elif symbol == '/':
            base_damage /= 2

    return base_damage


def process_demons(demons_input: str) -> list[str]:
    """
    Processes the input string of demon names, calculates health and damage,
    and returns a formatted list sorted by demon names.
    """
    demons = [demon.strip() for demon in demons_input.split(',') if demon.strip()]
    demons_info = {}

    for demon in demons:
        health = calculate_demon_health(demon)
        damage = calculate_demon_damage(demon)
        demons_info[demon] = (health, damage)

    sorted_demons = sorted(demons_info.items())

    return [f'{demon} - {stats[0]} health, {stats[1]:.2f} damage' for demon, stats in sorted_demons]


if __name__ == '__main__':
    demons_input = input()
    results_output = process_demons(demons_input=demons_input)

    for result in results_output:
        print(result)
