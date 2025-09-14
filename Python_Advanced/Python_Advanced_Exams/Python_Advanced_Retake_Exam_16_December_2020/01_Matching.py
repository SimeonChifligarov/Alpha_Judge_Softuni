from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())

matches = 0

while males and females:
    while females and (females[0] <= 0 or females[0] % 25 == 0):
        if not females:
            break
        if females[0] <= 0:
            females.popleft()
        elif females[0] % 25 == 0:
            females.popleft()
            if females:
                females.popleft()
    while males and (males[-1] <= 0 or males[-1] % 25 == 0):
        if not males:
            break
        if males and males[-1] <= 0:
            males.pop()
        elif males and males[-1] % 25 == 0:
            males.pop()
            if males:
                males.pop()
    if not males or not females:
        break
    f = females[0]
    m = males[-1]
    if m == f:
        matches += 1
        females.popleft()
        males.pop()
    else:
        females.popleft()
        males[-1] = m - 2

print(f"Matches: {matches}")
if males:
    print("Males left: " + ", ".join(map(str, males[::-1])))
else:
    print("Males left: none")
if females:
    print("Females left: " + ", ".join(map(str, females)))
else:
    print("Females left: none")
