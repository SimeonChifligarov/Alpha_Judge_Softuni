def process_explosions(data: str) -> str:
    """Processes 'explosions' in `data` where '>' consumes following characters based on strength."""
    result = []
    total_strength = 0

    i = 0
    while i < len(data):
        char = data[i]
        if char == '>':
            result.append(char)
            if i + 1 < len(data) and data[i + 1].isdigit():
                total_strength += int(data[i + 1])
        elif total_strength > 0:
            total_strength -= 1
        else:
            result.append(char)
        i += 1

    return ''.join(result)


if __name__ == '__main__':
    data_input: str = input().strip()

    result: str = process_explosions(data_input)
    print(result)
