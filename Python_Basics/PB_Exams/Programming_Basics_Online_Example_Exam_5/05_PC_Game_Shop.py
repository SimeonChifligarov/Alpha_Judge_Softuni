hearthstone_count = 0
fornite_count = 0
overwatch_count = 0
others_count = 0

games_sold = int(input())
for _ in range(games_sold):
    game = input()
    if game == 'Hearthstone':
        hearthstone_count += 1
    elif game == 'Fornite':
        fornite_count += 1
    elif game == 'Overwatch':
        overwatch_count += 1
    else:
        others_count += 1

print(f'Hearthstone - {(hearthstone_count / games_sold):.2%}')
print(f'Fornite - {(fornite_count / games_sold):.2%}')
print(f'Overwatch - {(overwatch_count / games_sold):.2%}')
print(f'Others - {(others_count / games_sold):.2%}')
