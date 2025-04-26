def is_coords_valid(x, y, mtrx):
    return 0 <= x < len(mtrx) and 0 <= y < len(mtrx[x])


size_of_field = int(input())

field = []
BUNNY_SYMBOL = 'B'
TRAP_SYMBOL = 'X'

for i in range(size_of_field):
    row = [el if el in [BUNNY_SYMBOL, TRAP_SYMBOL] else int(el) for el in input().split()]
    field.append(row)
    if BUNNY_SYMBOL in row:
        starting_bunny_position = (i, row.index(BUNNY_SYMBOL))

right_result = 0
right_moves = 0
left_result = 0
left_moves = 0
up_result = 0
up_moves = 0
down_result = 0
down_moves = 0

bunny_row = field[starting_bunny_position[0]]
bunny_col = []
for r in field:
    bunny_col.append(r[starting_bunny_position[1]])

# print(bunny_col)

for el in bunny_row[::-1]:
    if el == TRAP_SYMBOL:
        right_result = 0
        right_moves = 0
    elif el == BUNNY_SYMBOL:
        break
    else:
        right_result += el
        right_moves += 1

# print(right_result)

for el in bunny_row:
    if el == TRAP_SYMBOL:
        left_result = 0
        left_moves = 0
    elif el == BUNNY_SYMBOL:
        break
    else:
        left_result += el
        left_moves += 1

# print(left_result)

for el in bunny_col:
    if el == TRAP_SYMBOL:
        up_result = 0
        up_moves = 0
    elif el == BUNNY_SYMBOL:
        break
    else:
        up_result += el
        up_moves += 1

# print(up_result)

for el in bunny_col[::-1]:
    if el == TRAP_SYMBOL:
        down_result = 0
        down_moves = 0
    elif el == BUNNY_SYMBOL:
        break
    else:
        down_result += el
        down_moves += 1

# print(down_result)

max_result = max(up_result, down_result, left_result, right_result)
max_result_direction = None
max_result_path = []
if max_result == up_result:
    max_result_direction = 'up'
    for i in range(up_moves):
        max_result_path.append(f'[{starting_bunny_position[0] - i - 1}, {starting_bunny_position[1]}]')
elif max_result == down_result:
    max_result_direction = 'down'
    for i in range(down_moves):
        max_result_path.append(f'[{starting_bunny_position[0] + i + 1}, {starting_bunny_position[1]}]')
elif max_result == left_result:
    max_result_direction = 'left'
    for i in range(left_moves):
        max_result_path.append(f'[{starting_bunny_position[0]}, {starting_bunny_position[1] - i - 1}]')
elif max_result == right_result:
    max_result_direction = 'right'
    for i in range(right_moves):
        max_result_path.append(f'[{starting_bunny_position[0]}, {starting_bunny_position[1] + i + 1}]')

MOVEMENT_MAPPER = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

if max_result >= 0:
    print(max_result_direction)
    print('\n'.join(max_result_path))
    print(max_result)
