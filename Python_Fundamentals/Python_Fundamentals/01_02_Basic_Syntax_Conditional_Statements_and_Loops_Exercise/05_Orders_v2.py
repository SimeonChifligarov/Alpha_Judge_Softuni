def calculate_order_price(price_per_capsule, days, capsules_per_day):
    if not (0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000):
        return None
    return price_per_capsule * days * capsules_per_day


if __name__ == '__main__':
    total_price = 0.0
    number_of_orders = int(input())
    for _ in range(number_of_orders):
        price = float(input())
        days_count = int(input())
        capsules_needed = int(input())
        order_price = calculate_order_price(
            price_per_capsule=price,
            days=days_count,
            capsules_per_day=capsules_needed
        )
        if order_price is not None:
            total_price += order_price
            print(f'The price for the coffee is: ${order_price:.2f}')
    print(f'Total: ${total_price:.2f}')
