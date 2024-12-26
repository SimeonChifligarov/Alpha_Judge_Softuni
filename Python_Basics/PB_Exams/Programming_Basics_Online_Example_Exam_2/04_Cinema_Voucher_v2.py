def calculate_voucher_spending(voucher_value):
    tickets_count = 0
    other_purchases_count = 0

    while True:
        purchase = input()
        if purchase == 'End':
            break

        if len(purchase) > 8:
            cost = ord(purchase[0]) + ord(purchase[1])
        else:
            cost = ord(purchase[0])

        if cost > voucher_value:
            break

        voucher_value -= cost
        if len(purchase) > 8:
            tickets_count += 1
        else:
            other_purchases_count += 1

    print(tickets_count)
    print(other_purchases_count)


voucher = int(input())
calculate_voucher_spending(voucher)
