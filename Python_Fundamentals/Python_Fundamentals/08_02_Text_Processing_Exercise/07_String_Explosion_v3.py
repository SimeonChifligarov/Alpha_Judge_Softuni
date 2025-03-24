def process_explosions(text: str) -> str:
    """Processes explosions in a string and removes affected characters."""
    result = []
    explosion_strength = 0

    for index in range(len(text)):
        if text[index] == '>':
            result.append(text[index])
            if index + 1 < len(text) and text[index + 1].isdigit():
                explosion_strength += int(text[index + 1])
        elif explosion_strength > 0:
            explosion_strength -= 1
        else:
            result.append(text[index])

    return ''.join(result)


if __name__ == '__main__':
    input_text = input()
    final_text = process_explosions(text=input_text)
    print(final_text)
