# 1.	Брой яйца, които има първият играч - цяло число в интервала [1 … 99]
# 2.	Брой яйца, които има вторият играч - цяло число в интервала [1 … 99]
# След това до получаване на команда 'End' се чете многократно един ред:
# 3.	Победител - текст - 'one' или 'two'

p1_eggs = int(input())
p2_eggs = int(input())

has_winner = False
command = input()
while command != 'End':
    winner = command
    if winner == 'one':
        p2_eggs -= 1
        if p2_eggs <= 0:
            print(f'Player two is out of eggs. Player one has {p1_eggs} eggs left.')
            has_winner = True
            break
    elif winner == 'two':
        p1_eggs -= 1
        if p1_eggs <= 0:
            print(f'Player one is out of eggs. Player two has {p2_eggs} eggs left.')
            has_winner = True
            break

    command = input()

if not has_winner:
    print(f'Player one has {p1_eggs} eggs left.')
    print(f'Player two has {p2_eggs} eggs left.')
