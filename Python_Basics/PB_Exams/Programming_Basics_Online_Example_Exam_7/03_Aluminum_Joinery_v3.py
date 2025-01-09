def calculate_order_price(count, window_type, delivery_option):
    if count < 10:
        return 'Invalid order'

    price_per_window = 0
    discount = 0

    if window_type == '90X130':
        price_per_window = 110
        if count > 60:
            discount = 0.08
        elif count > 30:
            discount = 0.05
    elif window_type == '100X150':
        price_per_window = 140
        if count > 80:
            discount = 0.10
        elif count > 40:
            discount = 0.06
    elif window_type == '130X180':
        price_per_window = 190
        if count > 50:
            discount = 0.12
        elif count > 20:
            discount = 0.07
    elif window_type == '200X300':
        price_per_window = 250
        if count > 50:
            discount = 0.14
        elif count > 25:
            discount = 0.09

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
