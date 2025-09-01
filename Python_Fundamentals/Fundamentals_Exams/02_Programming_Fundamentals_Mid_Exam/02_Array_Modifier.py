arr = list(map(int, input().split()))

while True:
    line = input()
    if line == "end":
        break
    parts = line.split()
    if parts[0] == "swap":
        i, j = int(parts[1]), int(parts[2])
        arr[i], arr[j] = arr[j], arr[i]
    elif parts[0] == "multiply":
        i, j = int(parts[1]), int(parts[2])
        arr[i] = arr[i] * arr[j]
    elif parts[0] == "decrease":
        arr = [x - 1 for x in arr]

print(", ".join(map(str, arr)))
