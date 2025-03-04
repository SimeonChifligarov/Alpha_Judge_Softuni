def redistribute_wealth(population: list[int], min_wealth: int) -> list[int] | str:
    """
    Redistributes wealth among the population so that no individual has less than min_wealth.
    If redistribution is not possible, returns "No equal distribution possible".
    """
    if sum(population) < len(population) * min_wealth:
        return 'No equal distribution possible'

    for _ in range(len(population)):
        for i, wealth in enumerate(population):
            if wealth < min_wealth:
                richest_index = population.index(max(population))
                transfer_amount = min_wealth - wealth
                population[richest_index] -= transfer_amount
                population[i] += transfer_amount
                # population[i] = min_wealth

    return population


if __name__ == '__main__':
    population_input = [int(el) for el in input().split(', ')]
    min_wealth_input = int(input())

    result = redistribute_wealth(population=population_input, min_wealth=min_wealth_input)
    print(result)
