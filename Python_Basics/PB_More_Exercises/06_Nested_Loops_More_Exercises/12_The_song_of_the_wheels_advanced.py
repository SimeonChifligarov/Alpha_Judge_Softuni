def find_password(control_value):
    count = 0
    password = None
    results = []

    for a in range(1, 10):
        for b in range(1, 10):
            if a < b:
                for c in range(1, 10):
                    for d in range(1, 10):
                        if c > d:
                            if a * b + c * d == control_value:
                                results.append(f'{a}{b}{c}{d}')
                                count += 1
                                if count == 4:
                                    password = f'{a}{b}{c}{d}'

    if results:
        print(' '.join(results))
        if password:
            print(f'Password: {password}')
        else:
            print('No!')
    else:
        print('No!')


ctrl_value = int(input())

if 4 <= ctrl_value <= 144:
    find_password(control_value=ctrl_value)
else:
    print('Invalid input! The control value must be between 4 and 144.')
