change = float(input())
change = int(change * 100)

coins = 0
coin_values = [200, 100, 50, 20, 10, 5, 2, 1]

for coin in coin_values:
    while change >= coin:
        change -= coin
        coins += 1

print(coins)
