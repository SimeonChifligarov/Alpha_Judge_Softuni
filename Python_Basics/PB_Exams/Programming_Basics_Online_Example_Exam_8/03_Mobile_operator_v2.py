def calculate_total_cost(data):
    plans = {
        'one': {
            'Small': 9.98,
            'Middle': 18.99,
            'Large': 25.98,
            'ExtraLarge': 35.99,
        },
        'two': {
            'Small': 8.58,
            'Middle': 17.09,
            'Large': 23.59,
            'ExtraLarge': 31.79,
        },
    }

    internet_fees = {
        'low': 5.50,
        'medium': 4.35,
        'high': 3.85,
    }

    monthly_fee = plans[data['term']][data['plan']]

    if data['internet'] == 'yes':
        if monthly_fee <= 10.00:
            monthly_fee += internet_fees['low']
        elif monthly_fee <= 30.00:
            monthly_fee += internet_fees['medium']
        else:
            monthly_fee += internet_fees['high']

    total_cost = monthly_fee * data['months']

    if data['term'] == 'two':
        total_cost *= 0.9625

    return f'{total_cost:.2f} lv.'


if __name__ == '__main__':
    user_data = {
        'term': input(),
        'plan': input(),
        'internet': input(),
        'months': int(input()),
    }

    result = calculate_total_cost(data=user_data)
    print(result)
