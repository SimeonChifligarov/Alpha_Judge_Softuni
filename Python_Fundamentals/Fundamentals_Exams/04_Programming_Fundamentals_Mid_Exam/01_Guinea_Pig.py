food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())
ok = True

for day in range(1, 31):
    food -= 0.3
    if food <= 0 or hay <= 0 or cover <= 0:
        ok = False
        break
    if day % 2 == 0:
        hay -= food * 0.05
        if hay <= 0:
            ok = False
            break
    if day % 3 == 0:
        cover -= weight / 3
        if cover <= 0:
            ok = False
            break

if ok:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print("Merry must go to the pet store!")
