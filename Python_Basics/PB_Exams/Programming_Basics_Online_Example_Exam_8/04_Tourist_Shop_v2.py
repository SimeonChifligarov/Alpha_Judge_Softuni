def calculate_equipment_cost(data):
    budget = data['budget']
    products = data['products']

    total_cost = 0
    product_count = 0

    for i, product in enumerate(products):
        name, price = product['name'], product['price']
        if (i + 1) % 3 == 0:
            price /= 2

        budget_left = budget - total_cost - price

        if budget_left < 0:
            return f'You don\'t have enough money!\nYou need {abs(budget_left):.2f} leva!'

        total_cost += price
        product_count += 1

    return f'You bought {product_count} products for {total_cost:.2f} leva.'


if __name__ == '__main__':
    budget_input = float(input())
    products_input = []

    while True:
        try:
            product_name = input()
            if product_name == 'Stop':
                break
            product_price = float(input())
            products_input.append({'name': product_name, 'price': product_price})
        except EOFError:
            break

    data_input = {
        'budget': budget_input,
        'products': products_input,
    }

    result = calculate_equipment_cost(data=data_input)
    print(result)
