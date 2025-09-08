pirate = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
max_health = int(input())
ended = False

while True:
    line = input()
    if line == "Retire":
        break
    parts = line.split()
    cmd = parts[0]
    if cmd == "Fire":
        idx = int(parts[1])
        dmg = int(parts[2])
        if 0 <= idx < len(warship):
            warship[idx] -= dmg
            if warship[idx] <= 0:
                print("You won! The enemy ship has sunken.")
                ended = True
                break
    elif cmd == "Defend":
        start = int(parts[1])
        end = int(parts[2])
        dmg = int(parts[3])
        if 0 <= start <= end < len(pirate):
            for i in range(start, end + 1):
                pirate[i] -= dmg
                if pirate[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    ended = True
                    break
            if ended:
                break
    elif cmd == "Repair":
        idx = int(parts[1])
        health = int(parts[2])
        if 0 <= idx < len(pirate):
            pirate[idx] = min(max_health, pirate[idx] + health)
    elif cmd == "Status":
        need = sum(1 for x in pirate if x < max_health * 0.2)
        print(f"{need} sections need repair.")

if not ended:
    print(f"Pirate ship status: {sum(pirate)}")
    print(f"Warship status: {sum(warship)}")
