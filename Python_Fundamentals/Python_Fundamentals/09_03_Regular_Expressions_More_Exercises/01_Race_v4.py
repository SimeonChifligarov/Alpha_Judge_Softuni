def extract_name_and_distance(data: str) -> tuple[str, int]:
    """Extracts the name (letters) and distance (sum of digits) from race data."""
    name = ''.join(char for char in data if char.isalpha())
    distance = sum(int(char) for char in data if char.isdigit())
    return name, distance


def process_race_results(participants: list[str], race_data: list[str]) -> list[str]:
    """
    Processes race results, extracting participant names and distances run.
    Returns the top three racers sorted by distance.
    """
    results = {racer: 0 for racer in participants}

    for data in race_data:
        name, distance = extract_name_and_distance(data)
        if name in results:
            results[name] += distance

    top_racers = sorted(results.items(), key=lambda x: x[1], reverse=True)[:3]

    placements = ['1st', '2nd', '3rd']
    return [f'{place} place: {name}' for place, (name, _) in zip(placements, top_racers)]


def main():
    participants = input().split(', ')
    race_data = []

    while (entry := input()) != 'end of race':
        race_data.append(entry)

    results = process_race_results(participants, race_data)

    print('\n'.join(results))


if __name__ == '__main__':
    main()
