from collections import deque

mg = list(map(int, input().split(", ")))
drinks = deque(map(int, input().split(", ")))

current = 0
while mg and drinks:
    dose = mg.pop() * drinks[0]
    if current + dose <= 300:
        current += dose
        drinks.popleft()
    else:
        drinks.rotate(-1)
        current = max(0, current - 30)

if drinks:
    print("Drinks left: " + ", ".join(map(str, drinks)))
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {current} mg caffeine.")
