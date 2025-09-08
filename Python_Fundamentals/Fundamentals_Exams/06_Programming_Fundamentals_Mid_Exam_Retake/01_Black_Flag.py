days = int(input())
daily = int(input())
target = float(input())
total = 0.0

for d in range(1, days + 1):
    total += daily
    if d % 3 == 0:
        total += daily * 0.5
    if d % 5 == 0:
        total *= 0.7

if total >= target:
    print(f"Ahoy! {total:.2f} plunder gained.")
else:
    print(f"Collected only {total / target * 100:.2f}% of the plunder.")
