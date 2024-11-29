# using Decimal

from decimal import Decimal

change = Decimal(input())
coins = 0
coin_values = [
    Decimal('2.00'),
    Decimal('1.00'),
    Decimal('0.50'),
    Decimal('0.20'),
    Decimal('0.10'),
    Decimal('0.05'),
    Decimal('0.02'),
    Decimal('0.01'),
]

for coin in coin_values:
    while change >= coin:
        change -= coin
        coins += 1

print(coins)
