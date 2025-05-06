def minimal_coin_sum(coins: list[int], target: int) -> None:
    """
    Find the smallest number of coins needed to reach the target sum using greedy approach.

    Args:
        coins: list of available coin values
        target: the total amount to reach

    Returns:
        None
    """
    coins.sort(reverse=True)
    taken = []
    total_used = 0

    for coin in coins:
        if target == 0:
            break
        count = target // coin
        if count > 0:
            taken.append((coin, count))
            total_used += count
            target -= coin * count

    if target != 0:
        print('Error')
        return

    print(f'Number of coins to take: {total_used}')
    for coin_value, quantity in taken:
        print(f'{quantity} coin(s) with value {coin_value}')


if __name__ == '__main__':
    coin_values = [int(el) for el in input().split(', ')]
    desired_sum = int(input())
    minimal_coin_sum(coins=coin_values, target=desired_sum)
