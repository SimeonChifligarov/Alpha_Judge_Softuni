from collections import deque

fuels = list(map(int, input().split()))
cons = deque(map(int, input().split()))
need = deque(map(int, input().split()))

reached = []
level = 1

while fuels and cons and need:
    f = fuels.pop()
    c = cons.popleft()
    if f - c >= need[0]:
        print(f"John has reached: Altitude {level}")
        reached.append(f"Altitude {level}")
        need.popleft()
        level += 1
    else:
        print(f"John did not reach: Altitude {level}")
        break

if not need:
    print("John has reached all the altitudes and managed to reach the top!")
elif not reached:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
else:
    print("John failed to reach the top.")
    print("Reached altitudes: " + ", ".join(reached))
