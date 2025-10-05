from collections import deque

money = deque(map(int, input().split()))
prices = deque(map(int, input().split()))
foods = 0

while money and prices:
    m = money.pop()
    p = prices.popleft()
    if m == p:
        foods += 1
    elif m > p:
        foods += 1
        diff = m - p
        if money:
            money[-1] += diff
        else:
            money.append(diff)
    else:
        pass

if foods >= 4:
    print(f"Gluttony of the day! Henry ate {foods} foods.")
elif foods == 0:
    print("Henry remained hungry. He will try next weekend again.")
elif foods == 1:
    print("Henry ate: 1 food.")
else:
    print(f"Henry ate: {foods} foods.")
