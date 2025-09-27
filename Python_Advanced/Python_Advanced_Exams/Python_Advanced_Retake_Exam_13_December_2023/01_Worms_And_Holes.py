from collections import deque

worms = list(map(int, input().split()))
holes = deque(map(int, input().split()))
initial_worms = len(worms)
matches = 0

while worms and holes:
    w = worms.pop()
    if w <= 0:
        continue
    h = holes.popleft()
    if w == h:
        matches += 1
    else:
        w -= 3
        if w > 0:
            worms.append(w)

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms:
    if matches == initial_worms:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")
else:
    print("Worms left: " + ", ".join(map(str, worms)))

if not holes:
    print("Holes left: none")
else:
    print("Holes left: " + ", ".join(map(str, holes)))
