import re


def decrypt_message(encrypted_message: str) -> str:
    """
    Decrypts the given encrypted message by reducing the ASCII value of each character
    based on the count of letters 's', 't', 'a', 'r' (case insensitive).
    """
    key = sum(1 for char in encrypted_message if char.lower() in 'star')
    return ''.join(chr(ord(char) - key) for char in encrypted_message)


def process_messages(messages: list[str]) -> list[str]:
    """
    Processes encrypted messages, decrypts them, and extracts relevant information.
    Returns formatted results of attacked and destroyed planets.
    """
    message_pattern = re.compile(r'''
        @(?P<planet>[A-Za-z]+)         # Planet name after '@', only letters
        [^@\-!:>]*                     # Any characters except the restricted ones
        :(?P<population>\d+)           # Population number after ':'
        [^@\-!:>]*                     # Any characters except the restricted ones
        !(?P<attack>[AD])!             # Attack type ('A' or 'D') surrounded by '!'
        [^@\-!:>]*                     # Any characters except the restricted ones
        ->(?P<soldiers>\d+)            # Soldier count after '->'
    ''', re.VERBOSE)

    attacked_planets = []
    destroyed_planets = []

    for encrypted_message in messages:
        decrypted_message = decrypt_message(encrypted_message)
        match = message_pattern.search(decrypted_message)

        if match:
            planet_name = match.group('planet')
            attack_type = match.group('attack')

            if attack_type == 'A':
                attacked_planets.append(planet_name)
            else:
                destroyed_planets.append(planet_name)

    attacked_planets.sort()
    destroyed_planets.sort()

    result = [
        f'Attacked planets: {len(attacked_planets)}',
        *[f'-> {planet}' for planet in attacked_planets],
        f'Destroyed planets: {len(destroyed_planets)}',
        *[f'-> {planet}' for planet in destroyed_planets]
    ]

    return result


if __name__ == '__main__':
    message_count = int(input())
    messages_input = [input() for _ in range(message_count)]

    results_output = process_messages(messages=messages_input)

    for res in results_output:
        print(res)
