# using while True

width = int(input())
length = int(input())
total_pieces = width * length

while True:
    command = input()
    if command == 'STOP':
        print(f'{total_pieces} pieces are left.')
        break
    pieces_taken = int(command)
    total_pieces -= pieces_taken

    if total_pieces <= 0:
        print(f'No more cake left! You need {abs(total_pieces)} pieces more.')
        break
