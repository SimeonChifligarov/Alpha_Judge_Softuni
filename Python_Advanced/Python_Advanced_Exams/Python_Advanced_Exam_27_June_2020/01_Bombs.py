from collections import deque

effects = deque(int(x) for x in input().split(", "))
casings = [int(x) for x in input().split(", ")]
targets = {40: "Datura Bombs", 60: "Cherry Bombs", 120: "Smoke Decoy Bombs"}
made = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}


def pouch_filled(d):
    return all(v >= 3 for v in d.values())


while effects and casings and not pouch_filled(made):
    s = effects[0] + casings[-1]
    if s in targets:
        made[targets[s]] += 1
        effects.popleft()
        casings.pop()
    else:
        casings[-1] -= 5
        if casings[-1] < 0:
            casings.pop()

if pouch_filled(made):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
print(f"Bomb Effects: {', '.join(map(str, effects)) if effects else 'empty'}")
print(f"Bomb Casings: {', '.join(map(str, casings)) if casings else 'empty'}")
print(f"Cherry Bombs: {made['Cherry Bombs']}")
print(f"Datura Bombs: {made['Datura Bombs']}")
print(f"Smoke Decoy Bombs: {made['Smoke Decoy Bombs']}")
