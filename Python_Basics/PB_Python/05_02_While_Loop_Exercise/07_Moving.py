width = int(input())
length = int(input())
height = int(input())

total_space = width * length * height
taken_space = 0

while taken_space < total_space:
    command = input()

    if command == 'Done':
        break

    boxes = int(command)
    taken_space += boxes

is_space_left = total_space >= taken_space
if is_space_left:
    print(f'{total_space - taken_space} Cubic meters left.')
else:
    print(f'No more free space! You need {taken_space - total_space} Cubic meters more.')
