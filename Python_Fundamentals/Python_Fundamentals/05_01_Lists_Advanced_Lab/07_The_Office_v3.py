def evaluate_happiness(happiness_levels: list[int], factor: int) -> str:
    """
    Multiplies each employee's happiness by the given factor and evaluates if the majority are happy.
    """
    adjusted_happiness = [level * factor for level in happiness_levels]
    average_happiness = sum(adjusted_happiness) / len(adjusted_happiness)
    happy_count = sum(1 for level in adjusted_happiness if level >= average_happiness)
    total_count = len(adjusted_happiness)

    return (
        f'Score: {happy_count}/{total_count}. '
        f'Employees are {"happy" if happy_count >= total_count / 2 else "not happy"}!'
    )


if __name__ == '__main__':
    happiness_levels_input = [int(num) for num in input().split()]
    factor_input = int(input())
    result = evaluate_happiness(happiness_levels=happiness_levels_input, factor=factor_input)
    print(result)
