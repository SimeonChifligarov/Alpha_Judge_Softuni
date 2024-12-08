season = input()
group_type = input()
students_count = int(input())
nights_count = int(input())

prices = {
    'Winter': {
        'boys': 9.60,
        'girls': 9.60,
        'mixed': 10.00,
    },
    'Spring': {
        'boys': 7.20,
        'girls': 7.20,
        'mixed': 9.50,
    },
    'Summer': {
        'boys': 15.00,
        'girls': 15.00,
        'mixed': 20.00,
    },
}

sports = {
    'Winter': {
        'boys': 'Judo',
        'girls': 'Gymnastics',
        'mixed': 'Ski',
    },
    'Spring': {
        'boys': 'Tennis',
        'girls': 'Athletics',
        'mixed': 'Cycling',
    },
    'Summer': {
        'boys': 'Football',
        'girls': 'Volleyball',
        'mixed': 'Swimming',
    },
}

price_per_night = prices[season][group_type]
total_price = price_per_night * students_count * nights_count

if students_count >= 50:
    total_price *= 0.50
elif students_count >= 20:
    total_price *= 0.85
elif students_count >= 10:
    total_price *= 0.95

sport = sports[season][group_type]
print(f'{sport} {total_price:.2f} lv.')
