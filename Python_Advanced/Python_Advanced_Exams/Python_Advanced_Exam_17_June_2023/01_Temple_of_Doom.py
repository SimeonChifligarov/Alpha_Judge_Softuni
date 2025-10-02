from collections import deque

tools = deque(map(int, input().split()))
substances = list(map(int, input().split()))
challenges = list(map(int, input().split()))

while tools and substances and challenges:
    t = tools[0]
    s = substances[-1]
    r = t * s
    if r in challenges:
        tools.popleft()
        substances.pop()
        challenges.remove(r)
    else:
        tools.popleft()
        tools.append(t + 1)
        substances[-1] -= 1
        if substances[-1] == 0:
            substances.pop()

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print("Tools: " + ", ".join(map(str, tools)))
if substances:
    print("Substances: " + ", ".join(map(str, substances)))
if challenges:
    print("Challenges: " + ", ".join(map(str, challenges)))
