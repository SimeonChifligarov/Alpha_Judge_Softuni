def calculate_coins(group_size: int, days: int) -> (int, int):
    coins = 0
    companions = group_size

    for day in range(1, days + 1):
        if day % 10 == 0:
            companions -= 2

        if day % 15 == 0:
            companions += 5

        coins += 50
        coins -= 2 * companions

        if day % 3 == 0:
            coins -= 3 * companions

        if day % 5 == 0:
            coins += 20 * companions
            if day % 3 == 0:
                coins -= 2 * companions

    return coins, companions


if __name__ == '__main__':
    group_size_input = int(input())
    days_input = int(input())
    total_coins, total_companions = calculate_coins(group_size=group_size_input, days=days_input)
    coins_per_companion = total_coins // total_companions
    print(f'{total_companions} companions received {coins_per_companion} coins each.')
