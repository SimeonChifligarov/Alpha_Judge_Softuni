towns = {}

while True:
    line = input()
    if line == "Sail":
        break
    town, pop, gold = line.split("||")
    pop = int(pop)
    gold = int(gold)
    if town not in towns:
        towns[town] = [pop, gold]
    else:
        towns[town][0] += pop
        towns[town][1] += gold

while True:
    line = input()
    if line == "End":
        break
    parts = line.split("=>")
    if parts[0] == "Plunder":
        town = parts[1]
        people = int(parts[2])
        gold = int(parts[3])
        towns[town][0] -= people
        towns[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if towns[town][0] <= 0 or towns[town][1] <= 0:
            del towns[town]
            print(f"{town} has been wiped off the map!")
    elif parts[0] == "Prosper":
        town = parts[1]
        gold = int(parts[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            towns[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {towns[town][1]} gold.")

if towns:
    print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
    for town, (pop, gold) in towns.items():
        print(f"{town} -> Population: {pop} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
