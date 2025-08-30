people = int(input())
wagons = list(map(int, input().split()))

for i in range(len(wagons)):
    free = 4 - wagons[i]
    if free <= 0 or people == 0:
        continue
    add = min(free, people)
    wagons[i] += add
    people -= add

has_empty = any(w < 4 for w in wagons)

if people == 0 and has_empty:
    print("The lift has empty spots!")
    print(' '.join(map(str, wagons)))
elif people > 0 and not has_empty:
    print(f"There isn't enough space! {people} people in a queue!")
    print(' '.join(map(str, wagons)))
else:
    print(' '.join(map(str, wagons)))
