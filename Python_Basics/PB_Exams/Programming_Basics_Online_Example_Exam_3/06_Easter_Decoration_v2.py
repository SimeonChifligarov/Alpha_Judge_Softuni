def easter_shop(customers_count):
    total_revenue = 0

    for _ in range(customers_count):
        total_price = 0
        items_count = 0

        while True:
            purchase = input()
            if purchase == 'Finish':
                break
            if purchase == 'basket':
                total_price += 1.50
            elif purchase == 'wreath':
                total_price += 3.80
            elif purchase == 'chocolate bunny':
                total_price += 7.00
            items_count += 1

        if items_count % 2 == 0:
            total_price *= 0.80

        total_revenue += total_price
        print(f'You purchased {items_count} items for {total_price:.2f} leva.')

    average_bill = total_revenue / customers_count
    print(f'Average bill per client is: {average_bill:.2f} leva.')


customers = int(input())
easter_shop(customers)
