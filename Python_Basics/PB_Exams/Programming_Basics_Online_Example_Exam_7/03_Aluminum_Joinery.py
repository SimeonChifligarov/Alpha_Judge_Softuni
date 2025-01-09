dogrami_count = int(input())  # rename variable
dogrami_type = input()  # rename variable
delivery = input()

price_per_one = 0
discount_percent = 0
total_price = 0

if dogrami_type == '90X130':
    price_per_one = 110
    if 30 < dogrami_count <= 60:
        discount_percent = 5
    elif dogrami_count > 60:
        discount_percent = 8
elif dogrami_type == '100X150':
    price_per_one = 140
    if 40 < dogrami_count <= 80:
        discount_percent = 6
    elif dogrami_count > 80:
        discount_percent = 10
elif dogrami_type == '130X180':
    price_per_one = 190
    if 20 < dogrami_count <= 50:
        discount_percent = 7
    elif dogrami_count > 50:
        discount_percent = 12
elif dogrami_type == '200X300':
    price_per_one = 250
    if 25 < dogrami_count <= 50:
        discount_percent = 9
    elif dogrami_count > 50:
        discount_percent = 14

total_price = price_per_one * dogrami_count * (100 - discount_percent) / 100

if delivery == 'With delivery':
    total_price += 60

if dogrami_count > 99:
    total_price *= 0.96

if dogrami_count < 10:
    print('Invalid order')
else:
    print(f'{total_price:.2f} BGN')
