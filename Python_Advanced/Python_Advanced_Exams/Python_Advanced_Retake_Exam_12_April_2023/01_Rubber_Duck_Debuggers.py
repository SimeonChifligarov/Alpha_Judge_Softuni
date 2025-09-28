from collections import deque

times = deque(map(int, input().split()))
tasks = list(map(int, input().split()))

ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

while times and tasks:
    t = times[0]
    s = tasks[-1]
    total = t * s
    if 0 <= total <= 60:
        ducks["Darth Vader Ducky"] += 1
        times.popleft()
        tasks.pop()
    elif 61 <= total <= 120:
        ducks["Thor Ducky"] += 1
        times.popleft()
        tasks.pop()
    elif 121 <= total <= 180:
        ducks["Big Blue Rubber Ducky"] += 1
        times.popleft()
        tasks.pop()
    elif 181 <= total <= 240:
        ducks["Small Yellow Rubber Ducky"] += 1
        times.popleft()
        tasks.pop()
    else:
        tasks[-1] -= 2
        times.append(times.popleft())

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {ducks['Darth Vader Ducky']}")
print(f"Thor Ducky: {ducks['Thor Ducky']}")
print(f"Big Blue Rubber Ducky: {ducks['Big Blue Rubber Ducky']}")
print(f"Small Yellow Rubber Ducky: {ducks['Small Yellow Rubber Ducky']}")
