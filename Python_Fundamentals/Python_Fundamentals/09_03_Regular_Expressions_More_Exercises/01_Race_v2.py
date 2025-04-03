import re


def process_race_results(participants: list[str], race_data: list[str]) -> list[str]:
    """
    Processes race results, extracting participant names and distances run.
    Returns the top three racers sorted by distance.
    """
    results = {racer: 0 for racer in participants}

    for data in race_data:
        name = ''.join(re.findall(r'[A-Za-z]', data))
        distance = sum(int(digit) for digit in re.findall(r'\d', data))

        if name in results:
            results[name] += distance

    sorted_racers = sorted(results.items(), key=lambda x: x[1], reverse=True)[:3]

    return [
        f'1st place: {sorted_racers[0][0]}',
        f'2nd place: {sorted_racers[1][0]}',
        f'3rd place: {sorted_racers[2][0]}'
    ]


if __name__ == '__main__':
    participants_input = [el for el in input().split(', ')]
    race_data_input = []

    while (entry := input()) != 'end of race':
        race_data_input.append(entry)

    results_output = process_race_results(participants=participants_input, race_data=race_data_input)

    for result in results_output:
        print(result)
