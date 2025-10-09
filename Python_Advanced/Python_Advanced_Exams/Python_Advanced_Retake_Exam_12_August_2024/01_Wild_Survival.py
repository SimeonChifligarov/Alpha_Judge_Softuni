from collections import deque

bees = deque(map(int, input().split()))
eaters = list(map(int, input().split()))

while bees and eaters:
    b = bees[0]
    e = eaters[-1]
    bb, ee = b, e
    while bb > 0 and ee > 0:
        if bb < 7:
            bb = 0
            break
        bb -= 7
        ee -= 1
    if bb == 0 and ee > 0:
        bees.popleft()
        eaters[-1] = ee
    elif ee == 0 and bb > 0:
        eaters.pop()
        bees.popleft()
        bees.append(bb)
    else:
        eaters.pop()
        bees.popleft()

print("The final battle is over!")
if not bees and not eaters:
    print("But no one made it out alive!")
elif bees:
    print("Bee groups left: " + ", ".join(map(str, bees)))
else:
    print("Bee-eater groups left: " + ", ".join(map(str, eaters)))
