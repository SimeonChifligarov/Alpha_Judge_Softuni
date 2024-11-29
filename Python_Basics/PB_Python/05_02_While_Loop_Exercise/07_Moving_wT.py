# using while True

width = int(input())
length = int(input())
height = int(input())

total_space = width * length * height
taken_space = 0

while True:
    command = input()

    if command == 'Done':
        if total_space > taken_space:
            print(f'{total_space - taken_space} Cubic meters left.')
        else:
            print(f'No more free space! You need {abs(total_space - taken_space)} Cubic meters more.')
        break

    boxes = int(command)
    taken_space += boxes

    if taken_space >= total_space:
        print(f'No more free space! You need {taken_space - total_space} Cubic meters more.')
        break
