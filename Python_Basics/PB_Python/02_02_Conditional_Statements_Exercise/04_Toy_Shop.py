puzzle_price = 2.60
doll_price = 3.00
bear_price = 4.10
minion_price = 8.20
truck_price = 2.00

trip_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
plush_bears = int(input())
minions = int(input())
trucks = int(input())

total_price = (
        puzzles * puzzle_price +
        talking_dolls * doll_price +
        plush_bears * bear_price +
        minions * minion_price +
        trucks * truck_price
)
total_toys = puzzles + talking_dolls + plush_bears + minions + trucks

if total_toys >= 50:
    total_price *= 0.75

total_price *= 0.90

if total_price >= trip_price:
    remaining_money = total_price - trip_price
    print(f'Yes! {remaining_money:.2f} lv left.')
else:
    needed_money = trip_price - total_price
    print(f'Not enough money! {needed_money:.2f} lv needed.')
