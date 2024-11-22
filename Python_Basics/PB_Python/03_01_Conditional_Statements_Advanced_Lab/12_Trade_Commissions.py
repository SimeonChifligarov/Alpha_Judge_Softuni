commisions = {
    'Sofia': {
        'small': 0.05,
        'medium': 0.07,
        'large': 0.08,
        'extra_large': 0.12,
    },
    'Varna': {
        'small': 0.045,
        'medium': 0.075,
        'large': 0.1,
        'extra_large': 0.13,
    },
    'Plovdiv': {
        'small': 0.055,
        'medium': 0.08,
        'large': 0.12,
        'extra_large': 0.145,
    }
}

city = input()
sales = float(input())

are_inputs_valid = city in commisions and sales >= 0
if are_inputs_valid:
    if sales <= 500:
        commission = commisions[city]['small']
    elif sales <= 1000:
        commission = commisions[city]['medium']
    elif sales <= 10000:
        commission = commisions[city]['large']
    else:
        commission = commisions[city]['extra_large']

    commission_amount = sales * commission
    print(f'{commission_amount:.2f}')
else:
    print('error')
