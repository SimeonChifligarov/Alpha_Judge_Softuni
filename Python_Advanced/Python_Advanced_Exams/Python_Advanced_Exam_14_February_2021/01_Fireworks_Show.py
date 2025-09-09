from collections import deque

effects = deque(int(x) for x in input().split(", "))
power = [int(x) for x in input().split(", ")]

palm = willow = crossette = 0


def enough():
    return palm >= 3 and willow >= 3 and crossette >= 3


while effects and power and not enough():
    while effects and effects[0] <= 0:
        effects.popleft()
    while power and power[-1] <= 0:
        power.pop()
    if not effects or not power or enough():
        break
    e = effects[0]
    p = power[-1]
    s = e + p
    if s % 3 == 0 and s % 5 != 0:
        palm += 1
        effects.popleft()
        power.pop()
    elif s % 5 == 0 and s % 3 != 0:
        willow += 1
        effects.popleft()
        power.pop()
    elif s % 3 == 0 and s % 5 == 0:
        crossette += 1
        effects.popleft()
        power.pop()
    else:
        effects.append(effects.popleft() - 1)

if enough():
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if effects:
    print("Firework Effects left: " + ", ".join(map(str, effects)))
if power:
    print("Explosive Power left: " + ", ".join(map(str, power)))
print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")
