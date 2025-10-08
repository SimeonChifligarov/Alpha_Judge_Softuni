from collections import deque

fifo = deque(map(int, input().split()))
lifo = list(map(int, input().split()))
target = int(input())

final_feed = []

while fifo and lifo:
    a = fifo.popleft()
    b = lifo.pop()
    if a == b:
        final_feed.append(0)
        continue
    if a > b:
        small, large, source = b, a, "fifo"
    else:
        small, large, source = a, b, "lifo"
    remainder = 0 if small == 0 else large % small
    if source == "lifo":
        final_feed.append(remainder)
        if remainder != 0:
            lifo.append(remainder * 2)
    else:
        final_feed.append(-remainder)
        if remainder != 0:
            fifo.append(remainder * 2)

print("Final Feed: " + ", ".join(map(str, final_feed)))
total = sum(final_feed)
if total >= target:
    print(f"Goal achieved! Engagement Value: {total}")
else:
    print(f"Goal not achieved! Short by: {target - total}")
