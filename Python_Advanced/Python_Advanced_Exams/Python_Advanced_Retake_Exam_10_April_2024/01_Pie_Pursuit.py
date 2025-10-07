from collections import deque

contestants = deque(map(int, input().split()))
pies = deque(map(int, input().split()))

while contestants and pies:
    c = contestants.popleft()
    p = pies.pop()
    if c >= p:
        c -= p
        if c > 0:
            contestants.append(c)
    else:
        p -= c
        if p == 1:
            if pies:
                pies[-1] += 1
            else:
                pies.append(1)
        else:
            pies.append(p)

if not pies and contestants:
    print("We will have to wait for more pies to be baked!")
    print("Contestants left: " + ", ".join(map(str, contestants)))
elif not pies and not contestants:
    print("We have a champion!")
else:
    print("Our contestants need to rest!")
    print("Pies left: " + ", ".join(map(str, pies)))
