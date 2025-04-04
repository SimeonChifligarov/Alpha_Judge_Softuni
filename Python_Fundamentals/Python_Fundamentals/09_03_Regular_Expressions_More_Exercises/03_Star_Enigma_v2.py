import re

DECRYPTION_LETTERS = {'s', 't', 'a', 'r'}


def decrypt_message(message: str) -> str:
    """Decrypts a message by shifting characters based on the count of specific letters."""
    key = sum(1 for char in message.lower() if char in DECRYPTION_LETTERS)
    return ''.join(chr(ord(char) - key) for char in message)


PLANET_PATTERN = re.compile(r"""
    @(?P<planet_name>[a-zA-Z]+)        # Planet name after @
    [^@!:>-]*                          # Ignore unwanted characters
    :(?P<planet_population>\d+)        # Population after :
    [^@!:>-]*                          # Ignore unwanted characters
    !(?P<attack_type>[AD])!            # Attack type (A or D) inside !
    [^@!:>-]*                          # Ignore unwanted characters
    ->(?P<soldiers_count>\d+)          # Soldiers count after ->
""", re.VERBOSE)


def process_messages(number_of_messages: int) -> tuple[list[str], list[str]]:
    """Processes input messages, decrypts them, and categorizes planets."""
    attacked_planets = []
    destroyed_planets = []

    for _ in range(number_of_messages):
        encrypted_message = input().strip()
        decrypted_message = decrypt_message(encrypted_message)

        match = PLANET_PATTERN.search(decrypted_message)
        if match:
            planet_data = match.groupdict()
            if planet_data["attack_type"] == "A":
                attacked_planets.append(planet_data["planet_name"])
            else:
                destroyed_planets.append(planet_data["planet_name"])

    return sorted(attacked_planets), sorted(destroyed_planets)


def main():
    """Handles input and output."""
    number_of_messages = int(input().strip())
    attacked_planets, destroyed_planets = process_messages(number_of_messages)

    print(f'Attacked planets: {len(attacked_planets)}')
    for planet in attacked_planets:
        print(f'-> {planet}')

    print(f'Destroyed planets: {len(destroyed_planets)}')
    for planet in destroyed_planets:
        print(f'-> {planet}')


if __name__ == '__main__':
    main()
