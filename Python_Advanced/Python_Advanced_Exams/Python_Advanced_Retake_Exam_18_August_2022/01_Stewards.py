from collections import deque

seats = input().split(", ")
first = deque(map(int, input().split(", ")))
second = deque(map(int, input().split(", ")))

available = set(seats)
matches = []
rotations = 0

while rotations < 10 and len(matches) < 3:
    a = first.popleft()
    b = second.pop()
    ch = chr(a + b)
    s1 = f"{a}{ch}"
    s2 = f"{b}{ch}"
    if s1 in available:
        matches.append(s1)
        available.remove(s1)
    elif s2 in available:
        matches.append(s2)
        available.remove(s2)
    else:
        first.append(a)
        second.appendleft(b)
    rotations += 1

print("Seat matches: " + ", ".join(matches))
print(f"Rotations count: {rotations}")
