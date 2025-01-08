def load_suitcases(trunk_capacity, suitcase_volumes):
    loaded_suitcases = 0
    current_capacity = trunk_capacity

    for index, volume in enumerate(suitcase_volumes, start=1):
        if index % 3 == 0:
            volume *= 1.10

        if volume > current_capacity:
            return f'No more space!\nStatistic: {loaded_suitcases} suitcases loaded.'

        current_capacity -= volume
        loaded_suitcases += 1

    return f'Congratulations! All suitcases are loaded!\nStatistic: {loaded_suitcases} suitcases loaded.'


if __name__ == '__main__':
    trunk_capacity_input = float(input())
    suitcase_volumes_input = []

    try:
        while True:
            command = input()
            if command == 'End':
                break
            suitcase_volumes_input.append(float(command))
    except EOFError:
        pass

    result = load_suitcases(trunk_capacity=trunk_capacity_input, suitcase_volumes=suitcase_volumes_input)
    print(result)
