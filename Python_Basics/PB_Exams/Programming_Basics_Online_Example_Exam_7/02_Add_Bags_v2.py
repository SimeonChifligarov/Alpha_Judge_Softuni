def calculate_baggage_price(base_price, weight, days_until_trip, baggage_count):
    if weight < 10:
        price_per_bag = base_price * 0.2
    elif weight <= 20:  # elif 10 <= weight <= 20:
        price_per_bag = base_price * 0.5
    else:
        price_per_bag = base_price

    if days_until_trip > 30:
        price_per_bag *= 1.1
    elif 7 <= days_until_trip <= 30:
        price_per_bag *= 1.15
    else:
        price_per_bag *= 1.4

    total_price = price_per_bag * baggage_count
    return f'The total price of bags is: {total_price:.2f} lv.'


if __name__ == '__main__':
    base_price_input = float(input())
    weight_input = float(input())
    days_until_trip_input = int(input())
    baggage_count_input = int(input())

    result = calculate_baggage_price(
        base_price=base_price_input,
        weight=weight_input,
        days_until_trip=days_until_trip_input,
        baggage_count=baggage_count_input
    )
    print(result)
