n = int(input())
total_weight = 0
total_cost = 0
van_weight = 0
truck_weight = 0
train_weight = 0

for _ in range(n):
    weight = int(input())
    total_weight += weight

    if weight <= 3:
        total_cost += weight * 200
        van_weight += weight
    elif 4 <= weight <= 11:
        total_cost += weight * 175
        truck_weight += weight
    else:
        total_cost += weight * 120
        train_weight += weight

average_price = total_cost / total_weight
van_percent = (van_weight / total_weight) * 100
truck_percent = (truck_weight / total_weight) * 100
train_percent = (train_weight / total_weight) * 100

print(f'{average_price:.2f}')
print(f'{van_percent:.2f}%')
print(f'{truck_percent:.2f}%')
print(f'{train_percent:.2f}%')
