from collections import deque

monsters = deque(int(x.strip()) for x in input().split(","))
strikes = [int(x.strip()) for x in input().split(",")]

killed = 0

while monsters and strikes:
    armor = monsters[0]
    strike = strikes[-1]
    if strike >= armor:
        killed += 1
        monsters.popleft()
        rem = strike - armor
        strikes.pop()
        if rem > 0:
            if strikes:
                strikes[-1] += rem
            else:
                strikes.append(rem)
    else:
        monsters.popleft()
        monsters.append(armor - strike)
        strikes.pop()

if not monsters:
    print("All monsters have been killed!")
if not strikes:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed}")
