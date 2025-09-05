neighborhood = list(map(int, input().split("@")))

pos = 0
while True:
    cmd = input()
    if cmd == "Love!":
        break
    _, length = cmd.split()
    pos += int(length)
    if pos >= len(neighborhood):
        pos = 0
    if neighborhood[pos] == 0:
        print(f"Place {pos} already had Valentine's day.")
    else:
        neighborhood[pos] -= 2
        if neighborhood[pos] == 0:
            print(f"Place {pos} has Valentine's day.")

print(f"Cupid's last position was {pos}.")
failed = sum(1 for x in neighborhood if x > 0)

if failed == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed} places.")
