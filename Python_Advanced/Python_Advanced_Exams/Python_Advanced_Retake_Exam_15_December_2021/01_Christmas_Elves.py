from collections import deque

elves = deque(map(int, input().split()))
boxes = list(map(int, input().split()))

toys = 0
energy_used = 0
turn = 0

while elves and boxes:
    elf = elves.popleft()
    if elf < 5:
        continue
    box = boxes[-1]
    turn += 1
    required = box
    produced = 1
    cookie = True
    if turn % 3 == 0:
        required *= 2
        produced = 2
    if turn % 5 == 0:
        produced = 0
        cookie = False
    if elf >= required:
        energy_used += required
        boxes.pop()
        toys += produced
        elf -= required
        if cookie:
            elf += 1
        elves.append(elf)
    else:
        elves.append(elf * 2)

print(f"Toys: {toys}")
print(f"Energy: {energy_used}")
if elves:
    print("Elves left: " + ", ".join(map(str, elves)))
if boxes:
    print("Boxes left: " + ", ".join(map(str, boxes)))
