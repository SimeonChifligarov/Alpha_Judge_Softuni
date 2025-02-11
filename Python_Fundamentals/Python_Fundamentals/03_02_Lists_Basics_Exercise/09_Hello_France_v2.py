def buy_and_sell_items(items_data: str, budget: float) -> None:
    """
    Processes items for purchase within a budget and calculates profit after reselling them.
    """
    
    item_limits = {
        'Clothes': 50.00,
        'Shoes': 35.00,
        'Accessories': 20.50,
    }

    items = items_data.split('|')
    bought_items = []
    total_spent = 0

    for item in items:
        item_type, price = item.split('->')
        price = float(price)

        if item_type in item_limits and price <= item_limits[item_type] and budget >= price:
            budget -= price
            total_spent += price
            bought_items.append(price * 1.4)

    profit = sum(bought_items) - total_spent
    final_budget = budget + sum(bought_items)

    print(' '.join(f'{price:.2f}' for price in bought_items))
    print(f'Profit: {profit:.2f}')
    if final_budget >= 150:
        print('Hello, France!')
    else:
        print('Not enough money.')


if __name__ == '__main__':
    items_input = input()
    budget_input = float(input())
    buy_and_sell_items(items_data=items_input, budget=budget_input)
