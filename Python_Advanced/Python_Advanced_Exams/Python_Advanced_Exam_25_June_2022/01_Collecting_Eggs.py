from collections import deque

eggs = deque(map(int, input().split(", ")))
papers = list(map(int, input().split(", ")))

boxes = 0

while eggs and papers:
    egg = eggs.popleft()
    if egg <= 0:
        continue
    if egg == 13:
        if len(papers) >= 2:
            papers[0], papers[-1] = papers[-1], papers[0]
        continue
    paper = papers.pop()
    if egg + paper <= 50:
        boxes += 1

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print("Eggs left: " + ", ".join(map(str, eggs)))
if papers:
    print("Pieces of paper left: " + ", ".join(map(str, papers)))
