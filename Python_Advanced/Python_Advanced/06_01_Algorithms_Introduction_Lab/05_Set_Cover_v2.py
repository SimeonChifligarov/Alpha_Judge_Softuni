def set_cover(universe: list[int], sets: list[list[int]]) -> list[list[int]] | None:
    """
    Choose the fewest sets that together cover the universe.

    Args:
        universe: list of elements to cover
        sets: list of available sets (as lists)

    Returns:
        The selected sets, or None if no full cover is possible
    """
    universe_set = set(universe)
    chosen_sets = []
    remaining_sets = sets.copy()

    while universe_set and remaining_sets:
        best_set = max(remaining_sets, key=lambda s: len(universe_set & set(s)))
        if not universe_set & set(best_set):
            break
        chosen_sets.append(best_set)
        universe_set -= set(best_set)
        remaining_sets.remove(best_set)

    if universe_set:
        return None
    return chosen_sets


if __name__ == '__main__':
    universe_input = [int(el) for el in input().split(', ')]
    number_of_sets = int(input())
    input_sets = [[int(el) for el in input().split(', ')] for _ in range(number_of_sets)]
    result = set_cover(universe=universe_input, sets=input_sets)

    if result is None:
        print('No solution exists')
    else:
        result = [sorted(s) for s in result]
        print(f'Sets to take ({len(result)}):')
        for s in result:
            print(f'{{ {", ".join(str(x) for x in s)} }}')
