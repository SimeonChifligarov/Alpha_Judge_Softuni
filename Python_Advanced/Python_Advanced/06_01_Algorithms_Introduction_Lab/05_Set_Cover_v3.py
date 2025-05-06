def set_cover(universe: list[int], sets: list[list[int]]) -> list[list[int]] | None:
    """
    Pick minimum sets to cover universe.

    Args:
        universe: elements to cover
        sets: available sets

    Returns:
        Chosen sets or None
    """
    needed = set(universe)
    chosen = []
    remaining = sets.copy()
    while needed:
        best = max(remaining, key=lambda s: len(needed & set(s)))
        if not needed & set(best):
            break
        chosen.append(best)
        needed -= set(best)
        remaining.remove(best)
    return None if needed else chosen


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
        [print(f'{{ {", ".join(str(x) for x in s)} }}') for s in result]
