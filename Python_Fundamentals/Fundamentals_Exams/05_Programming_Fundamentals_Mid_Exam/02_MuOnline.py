rooms = input().split("|")

health = 100
bitcoins = 0

for i, room in enumerate(rooms, 1):
    cmd, num = room.split()
    num = int(num)
    if cmd == "potion":
        heal = min(100 - health, num)
        health += heal
        print(f"You healed for {heal} hp.")
        print(f"Current health: {health} hp.")
    elif cmd == "chest":
        bitcoins += num
        print(f"You found {num} bitcoins.")
    else:
        health -= num
        if health > 0:
            print(f"You slayed {cmd}.")
        else:
            print(f"You died! Killed by {cmd}.")
            print(f"Best room: {i}")
            break
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
