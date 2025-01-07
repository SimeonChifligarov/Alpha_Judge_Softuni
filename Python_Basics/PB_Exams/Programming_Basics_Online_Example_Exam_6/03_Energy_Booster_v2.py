def calculate_order_cost(fruit, size, sets_count):
    prices = {
        'Watermelon': {'small': 56, 'big': 28.70},
        'Mango': {'small': 36.66, 'big': 19.60},
        'Pineapple': {'small': 42.10, 'big': 24.80},
        'Raspberry': {'small': 20, 'big': 15.20},
    }
    pieces_per_set = {'small': 2, 'big': 5}

    price_per_piece = prices[fruit][size]
    total_price = price_per_piece * pieces_per_set[size] * sets_count

    if 400 <= total_price <= 1000:
        total_price *= 0.85
    elif total_price > 1000:
        total_price *= 0.50

    return f'{total_price:.2f} lv.'


if __name__ == '__main__':
    fruit_input = input()
    size_input = input()
    sets_count_input = int(input())
    result = calculate_order_cost(fruit=fruit_input, size=size_input, sets_count=sets_count_input)
    print(result)
