def process_orders(orders):
    total_price = 0.0
    results = []
    for price_per_capsule, days, capsules_per_day in orders:
        order_price = calculate_order_price(
            price_per_capsule=price_per_capsule,
            days=days,
            capsules_per_day=capsules_per_day
        )
        if order_price is not None:
            total_price += order_price
            results.append(f'The price for the coffee is: ${order_price:.2f}')
    results.append(f'Total: ${total_price:.2f}')
    return results


def calculate_order_price(price_per_capsule, days, capsules_per_day):
    if not (0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000):
        return None
    return price_per_capsule * days * capsules_per_day


if __name__ == '__main__':
    number_of_orders = int(input())
    orders_list = [
        (float(input()), int(input()), int(input())) for _ in range(number_of_orders)
    ]
    res = process_orders(orders=orders_list)
    [print(r) for r in res]
