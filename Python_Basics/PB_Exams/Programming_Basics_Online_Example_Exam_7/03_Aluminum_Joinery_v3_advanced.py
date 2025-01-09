def calculate_order_price(count, window_type, delivery_option):
    if count < 10:
        return 'Invalid order'

    prices = {
        '90X130': 110,
        '100X150': 140,
        '130X180': 190,
        '200X300': 250,
    }

    discounts = {
        '90X130': [(30, 0.05), (60, 0.08)],
        '100X150': [(40, 0.06), (80, 0.10)],
        '130X180': [(20, 0.07), (50, 0.12)],
        '200X300': [(25, 0.09), (50, 0.14)],
    }

    price_per_window = prices[window_type]
    discount = 0

    for threshold, rate in discounts[window_type]:
        if count > threshold:
            discount = rate

    total_price = price_per_window * count * (1 - discount)

    if delivery_option == 'With delivery':
        total_price += 60

    if count > 99:
        total_price *= 0.96

    return f'{total_price:.2f} BGN'


if __name__ == '__main__':
    count_input = int(input())
    window_type_input = input()
    delivery_option_input = input()

    result = calculate_order_price(
        count=count_input,
        window_type=window_type_input,
        delivery_option=delivery_option_input
    )
    print(result)
