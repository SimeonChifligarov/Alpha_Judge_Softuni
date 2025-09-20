from collections import deque

food = list(map(int, input().split(", ")))
stamina = deque(map(int, input().split(", ")))

peaks = [("Vihren", 80), ("Kutelo", 90), ("Banski Suhodol", 100), ("Polezhan", 60), ("Kamenitza", 70)]
conquered = []
i = 0

while food and stamina and i < len(peaks):
    total = food.pop() + stamina.popleft()
    if total >= peaks[i][1]:
        conquered.append(peaks[i][0])
        i += 1

if len(conquered) == len(peaks):
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered:
    print("Conquered peaks:")
    for name in conquered:
        print(name)
