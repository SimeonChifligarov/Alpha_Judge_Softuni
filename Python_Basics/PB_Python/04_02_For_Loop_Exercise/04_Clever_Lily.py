age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

total_money = 0
toys_count = 0

for birthday in range(1, age + 1, 2):
    toys_count += 1

for birthday in range(2, age + 1, 2):
    money_from_birthday = birthday * 5  # 10 * (birthday // 2)
    total_money += money_from_birthday - 1

toys_money = toys_count * toy_price
total_money += toys_money

if total_money >= washing_machine_price:
    print(f'Yes! {total_money - washing_machine_price:.2f}')
else:
    print(f'No! {washing_machine_price - total_money:.2f}')
