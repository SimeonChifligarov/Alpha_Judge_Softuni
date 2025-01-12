def calculate_safari_cost(data):
    rates = {
        'fuel_rate': 2.10,
        'guide_fee': 100,
        'Saturday_discount': 0.90,
        'Sunday_discount': 0.80,
    }

    fuel_expense = data['fuel_amount'] * rates['fuel_rate']
    total_expense = fuel_expense + rates['guide_fee']

    if data['day'] == 'Saturday':
        total_expense *= rates['Saturday_discount']
    elif data['day'] == 'Sunday':
        total_expense *= rates['Sunday_discount']

    if data['budget'] >= total_expense:
        return f"Safari time! Money left: {(data['budget'] - total_expense):.2f} lv."
    else:
        return f"Not enough money! Money needed: {(total_expense - data['budget']):.2f} lv."


if __name__ == '__main__':
    user_data = {
        'budget': float(input()),
        'fuel_amount': float(input()),
        'day': input(),
    }

    result = calculate_safari_cost(data=user_data)
    print(result)
