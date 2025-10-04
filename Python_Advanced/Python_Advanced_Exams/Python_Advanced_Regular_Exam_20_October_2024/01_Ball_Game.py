from collections import deque

strengths = list(map(int, input().split()))
accuracies = deque(map(int, input().split()))

goals = 0

while strengths and accuracies:
    s = strengths[-1]
    a = accuracies[0]
    total = s + a
    if total == 100:
        strengths.pop()
        accuracies.popleft()
        goals += 1
    elif total < 100:
        if s < a:
            strengths.pop()
        elif s > a:
            accuracies.popleft()
        else:
            strengths.pop()
            accuracies.popleft()
            strengths.append(s + a)
    else:
        strengths.pop()
        strengths.append(s - 10)
        accuracies.append(accuracies.popleft())

if goals == 3:
    print("Paul scored a hat-trick!")
elif goals == 0:
    print("Paul failed to score a single goal.")
elif goals > 3:
    print("Paul performed remarkably well!")
else:
    print("Paul failed to make a hat-trick.")

if goals > 0:
    print(f"Goals scored: {goals}")

if strengths:
    print("Strength values left: " + ", ".join(map(str, strengths)))
if accuracies:
    print("Accuracy values left: " + ", ".join(map(str, accuracies)))
