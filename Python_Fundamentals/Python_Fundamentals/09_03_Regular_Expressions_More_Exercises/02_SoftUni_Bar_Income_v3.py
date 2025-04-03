import re


def process_orders(orders: list[str]) -> list[str]:
    """
    Processes orders, extracting customer, product, count, and price.
    Returns a list of formatted order strings and total income.
    """
    order_pattern = r'%([A-Z][a-z]+)%.*?<([\w]+)>.*?\|(\d+)\|.*?([\d]+(\.\d+)?)\$'
    total_income = 0
    processed_orders = []

    for order in orders:
        match = re.search(order_pattern, order)
        if match:
            customer_name = match.group(1)
            product = match.group(2)
            count = int(match.group(3))
            price = float(match.group(4))
            total_price = count * price
            total_income += total_price
            processed_orders.append(f'{customer_name}: {product} - {total_price:.2f}')

    processed_orders.append(f'Total income: {total_income:.2f}')
    return processed_orders


if __name__ == '__main__':
    orders_input = []

    while (order_entry := input()) != 'end of shift':
        orders_input.append(order_entry)

    orders_output = process_orders(orders=orders_input)

    for order in orders_output:
        print(order)
