def play_pokemon_dont_go(distances: list[int], indexes: list[int]) -> int:
    """
    Simulates capturing pokemon by modifying a sequence of distances based on given indexes.
    Returns the sum of all removed elements.
    """
    total_sum = 0

    while distances:
        # if not indexes:
        #     return total_sum

        index = indexes.pop(0)

        if index < 0:
            removed_element = distances.pop(0)
            distances.insert(0, distances[-1])
        elif index >= len(distances):
            removed_element = distances.pop(-1)
            distances.append(distances[0])
        else:
            removed_element = distances.pop(index)

        total_sum += removed_element
        distances = [
            el + removed_element if el <= removed_element else el - removed_element
            for el in distances
        ]

    return total_sum


if __name__ == '__main__':
    distances_input = [int(el) for el in input().split()]
    indexes_input = []

    while True:
        try:
            idx = int(input())
            indexes_input.append(idx)
        except (EOFError, ValueError):
            break

    result = play_pokemon_dont_go(distances=distances_input, indexes=indexes_input)
    print(result)
