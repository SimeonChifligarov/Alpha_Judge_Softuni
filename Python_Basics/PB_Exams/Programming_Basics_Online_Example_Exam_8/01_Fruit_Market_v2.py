def calculate_total_cost(strawberry_price, bananas_kg, oranges_kg, raspberries_kg, strawberries_kg):
    raspberry_price = strawberry_price / 2
    orange_price = raspberry_price * 0.6
    banana_price = raspberry_price * 0.2

    total_cost = (
        (strawberry_price * strawberries_kg) +
        (raspberry_price * raspberries_kg) +
        (orange_price * oranges_kg) +
        (banana_price * bananas_kg)
    )

    return f'{total_cost:.2f}'


if __name__ == '__main__':
    strawberry_price_input = float(input())
    bananas_kg_input = float(input())
    oranges_kg_input = float(input())
    raspberries_kg_input = float(input())
    strawberries_kg_input = float(input())

    result = calculate_total_cost(
        strawberry_price=strawberry_price_input,
        bananas_kg=bananas_kg_input,
        oranges_kg=oranges_kg_input,
        raspberries_kg=raspberries_kg_input,
        strawberries_kg=strawberries_kg_input,
    )
    print(result)
