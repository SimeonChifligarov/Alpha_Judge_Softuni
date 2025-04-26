# from pprint import pprint


def is_coords_valid(x, y, mtrx):
    return 0 <= x < len(mtrx) and 0 <= y < len(mtrx[x])


size_of_field = int(input())

field = []
BUNNY_SYMBOL = 'B'
TRAP_SYMBOL = 'X'

# SOLUTION No1
starting_bunny_position = None
max_eggs_collected = 0
max_eggs_movement_position = None
max_eggs_track = []

POSITION_MAPPERS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for i in range(size_of_field):
    row = [el if el in [BUNNY_SYMBOL, TRAP_SYMBOL] else int(el) for el in input().split()]
    field.append(row)
    if BUNNY_SYMBOL in row:
        starting_bunny_position = (i, row.index(BUNNY_SYMBOL))

# pprint(field)
# print(bunny_position)


for pos, move in POSITION_MAPPERS.items():
    current_eggs = 0
    current_eggs_track = []
    bunny_position = starting_bunny_position
    next_pos = (bunny_position[0] + move[0]), (bunny_position[1] + move[1])
    while is_coords_valid(next_pos[0], next_pos[1], field):
        if field[next_pos[0]][next_pos[1]] == TRAP_SYMBOL:
            break

        current_eggs += field[next_pos[0]][next_pos[1]]
        # if not field[next_pos[0]][next_pos[1]] == 0:
        #     current_eggs_track.append([next_pos[0], next_pos[1]])
        current_eggs_track.append([next_pos[0], next_pos[1]])
        next_pos = (next_pos[0] + move[0]), (next_pos[1] + move[1])

    if current_eggs >= max_eggs_collected:
        max_eggs_collected = current_eggs
        max_eggs_movement_position = pos
        max_eggs_track = current_eggs_track

result = []
result.append(max_eggs_movement_position)
# result.extend([str(el) for el in max_eggs_track])
for tr in max_eggs_track:
    result.append(tr)
result.append(max_eggs_collected)

# print(result)

for r in result:
    if r is not None:
        print(r)
