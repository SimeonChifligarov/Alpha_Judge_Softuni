from collections import deque

packages = deque(map(int, input().split()))
couriers = deque(map(int, input().split()))
total = 0

while packages and couriers:
    p = packages.pop()
    c = couriers.popleft()
    if c >= p:
        total += p
        if c > p:
            c -= 2 * p
            if c > 0:
                couriers.append(c)
    else:
        total += c
        p -= c
        packages.append(p)

print(f"Total weight: {total} kg")
if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    print("Unfortunately, there are no more available couriers to deliver the following packages: " + ", ".join(
        map(str, packages)))
elif couriers and not packages:
    print(
        "Couriers are still on duty: " + ", ".join(map(str, couriers)) + " but there are no more packages to deliver.")
