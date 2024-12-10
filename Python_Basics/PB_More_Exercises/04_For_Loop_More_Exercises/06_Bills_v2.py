water = 20
internet = 15

months = int(input())

electricity_bills = []

for _ in range(months):
    electricity_bills.append(float(input()))

total_electricity = 0
total_water = 0
total_internet = 0
total_other = 0

for electricity in electricity_bills:
    total_electricity += electricity
    total_water += water
    total_internet += internet

    other = 1.20 * (electricity + water + internet)
    total_other += other

average = (total_electricity + total_water + total_internet + total_other) / months

print(f'Electricity: {total_electricity:.2f} lv')
print(f'Water: {total_water:.2f} lv')
print(f'Internet: {total_internet:.2f} lv')
print(f'Other: {total_other:.2f} lv')
print(f'Average: {average:.2f} lv')
