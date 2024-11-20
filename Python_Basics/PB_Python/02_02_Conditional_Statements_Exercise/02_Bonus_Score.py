initial_points = int(input())

if initial_points <= 100:
    bonus_points = 5
elif initial_points <= 1_000:
    bonus_points = initial_points * 0.20
else:
    bonus_points = initial_points * 0.10

if initial_points % 2 == 0:
    bonus_points += 1
if initial_points % 10 == 5:
    bonus_points += 2

total_points = initial_points + bonus_points

print(bonus_points)
print(total_points)
