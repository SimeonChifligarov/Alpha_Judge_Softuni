# using while True
ERROR_MSG = 'Error in transaction!'
SOLD_MSG = 'Product sold!'
FAILED_MSG = 'Failed to collect required money for charity.'

target_amount = int(input())

total_cash = 0
total_card = 0
cash_count = 0
card_count = 0
is_cash = True

while True:
    command = input()

    if command == 'End':
        print(FAILED_MSG)
        break

    product_price = int(command)

    if product_price > 100 and is_cash:
        print(ERROR_MSG)
    elif product_price < 10 and not is_cash:
        print(ERROR_MSG)
    elif is_cash:
        total_cash += product_price
        cash_count += 1
        print(SOLD_MSG)
    else:
        total_card += product_price
        card_count += 1
        print(SOLD_MSG)

    if total_cash + total_card >= target_amount:
        print(f'Average CS: {(total_cash / cash_count):.2f}')
        print(f'Average CC: {(total_card / card_count):.2f}')
        break

    is_cash = not is_cash
