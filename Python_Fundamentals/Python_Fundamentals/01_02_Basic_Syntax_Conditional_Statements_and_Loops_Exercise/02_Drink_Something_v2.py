def determine_drink(age):
    if age <= 14:
        return 'toddy'
    elif age <= 18:
        return 'coke'
    elif age <= 21:
        return 'beer'
    else:
        return 'whisky'


if __name__ == '__main__':
    age_input = int(input())
    drink = determine_drink(age=age_input)
    print(f'drink {drink}')
