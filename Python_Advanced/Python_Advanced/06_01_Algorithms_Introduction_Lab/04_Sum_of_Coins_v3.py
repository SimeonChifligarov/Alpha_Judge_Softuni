def minimal_coin_sum(coins: list[int], target: int) -> None:
    """
    Use fewest coins to reach sum.

    Args:
        coins: coin denominations
        target: total amount

    Returns:
        None
    """
    coins.sort(reverse=True)
    used = []
    total = 0
    for coin in coins:
        count = target // coin
        if count:
            used.append((coin, count))
            total += count
            target -= coin * count
        if target == 0:
            break
    if target != 0:
        print('Error')
        return
    print(f'Number of coins to take: {total}')
    [print(f'{qty} coin(s) with value {val}') for val, qty in used]


if __name__ == '__main__':
    coin_values = [int(el) for el in input().split(', ')]
    desired_sum = int(input())
    minimal_coin_sum(coins=coin_values, target=desired_sum)
