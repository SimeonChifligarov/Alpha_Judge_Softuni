def calculate_price(city, package, vip_discount, days):
    prices = {
        'Bansko': {'withEquipment': 100, 'noEquipment': 80},
        'Borovets': {'withEquipment': 100, 'noEquipment': 80},
        'Varna': {'withBreakfast': 130, 'noBreakfast': 100},
        'Burgas': {'withBreakfast': 130, 'noBreakfast': 100},
    }

    discounts = {
        'Bansko': {'withEquipment': 0.10, 'noEquipment': 0.05},
        'Borovets': {'withEquipment': 0.10, 'noEquipment': 0.05},
        'Varna': {'withBreakfast': 0.12, 'noBreakfast': 0.07},
        'Burgas': {'withBreakfast': 0.12, 'noBreakfast': 0.07},
    }

    if city not in prices or package not in prices[city] or days < 1:
        if days < 1:
            print('Days must be positive number!')
        else:
            print('Invalid input!')
        return

    base_price = prices[city][package]
    if vip_discount == 'yes':
        base_price *= 1 - discounts[city][package]

    total_price = base_price * days
    if days > 7:
        total_price -= base_price

    print(f'The price is {total_price:.2f}lv! Have a nice time!')


city_name = input()
package_type = input()
vip_status = input()
stay_days = int(input())

calculate_price(city=city_name, package=package_type, vip_discount=vip_status, days=stay_days)
