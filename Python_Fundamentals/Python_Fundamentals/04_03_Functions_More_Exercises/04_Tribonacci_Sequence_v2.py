num = int(input())

trib = [1, 1, 2]
for _ in range(3, num):
    trib.append(trib[-1] + trib[-2] + trib[-3])

print(*trib[:num])
