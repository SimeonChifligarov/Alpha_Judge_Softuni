VIP_TICKET_PRICE = 499.99
NORMAL_TICKET_PRICE = 249.99

budget = float(input())
ticket_category = input()  # 'VIP' or 'Normal'
fans_count = int(input())

transport_cost_as_percent = 0
if fans_count < 4:
    transport_cost_as_percent = 0.75
elif fans_count < 10:
    transport_cost_as_percent = 0.60
elif fans_count < 25:
    transport_cost_as_percent = 0.50
elif fans_count < 50:
    transport_cost_as_percent = 0.40
else:  # elif fans_count >= 50:
    transport_cost_as_percent = 0.25

ticket_price = 0
if ticket_category == 'VIP':
    ticket_price = VIP_TICKET_PRICE
elif ticket_category == 'Normal':
    ticket_price = NORMAL_TICKET_PRICE

available_money = budget * (1 - transport_cost_as_percent)
needed_money = fans_count * ticket_price

if available_money >= needed_money:
    money_left = available_money - needed_money
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    extra_money_needed = needed_money - available_money
    print(f'Not enough money! You need {extra_money_needed:.2f} leva.')
