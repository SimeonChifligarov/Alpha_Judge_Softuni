n = int(input())
heroes = {}

for _ in range(n):
    name, hp, mp = input().split()
    heroes[name] = {"HP": int(hp), "MP": int(mp)}

while True:
    command = input()
    if command == "End":
        break

    parts = command.split(" - ")
    action = parts[0]
    hero = parts[1]

    if action == "CastSpell":
        mp_needed = int(parts[2])
        spell = parts[3]
        if heroes[hero]["MP"] >= mp_needed:
            heroes[hero]["MP"] -= mp_needed
            print(f"{hero} has successfully cast {spell} and now has {heroes[hero]['MP']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell}!")

    elif action == "TakeDamage":
        damage = int(parts[2])
        attacker = parts[3]
        heroes[hero]["HP"] -= damage
        if heroes[hero]["HP"] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['HP']} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            del heroes[hero]

    elif action == "Recharge":
        amount = int(parts[2])
        before = heroes[hero]["MP"]
        heroes[hero]["MP"] = min(200, heroes[hero]["MP"] + amount)
        print(f"{hero} recharged for {heroes[hero]['MP'] - before} MP!")

    elif action == "Heal":
        amount = int(parts[2])
        before = heroes[hero]["HP"]
        heroes[hero]["HP"] = min(100, heroes[hero]["HP"] + amount)
        print(f"{hero} healed for {heroes[hero]['HP'] - before} HP!")

for hero, stats in heroes.items():
    print(f"{hero}")
    print(f"  HP: {stats['HP']}")
    print(f"  MP: {stats['MP']}")
