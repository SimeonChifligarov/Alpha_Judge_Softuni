month = input()
nights = int(input())

studio_price = 0
apartment_price = 0
discount = 0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if nights > 14:
        discount = 0.30
    elif nights > 7:
        discount = 0.05
elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        discount = 0.20
elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77

studio_price -= studio_price * discount

if nights > 14:
    apartment_price -= apartment_price * 0.10

studio_total = studio_price * nights
apartment_total = apartment_price * nights

print(f'Apartment: {apartment_total:.2f} lv.')
print(f'Studio: {studio_total:.2f} lv.')
