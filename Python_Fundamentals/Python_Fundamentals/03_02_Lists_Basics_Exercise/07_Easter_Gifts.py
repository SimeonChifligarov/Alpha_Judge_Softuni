# •	On the 1st line you are going to receive the names of the gifts, separated by a single space.
# •	On the next lines, until the 'No Money' command is received, you will be receiving commands.
# •	The input will always be valid.

list_of_gifts = input().split()

command = input()
current_command_list = []
current_gift = ''
while not command == 'No Money':
    current_command_list = command.split()
    current_gift = current_command_list[1]
    if current_command_list[0] == 'OutOfStock':
        for index in range(len(list_of_gifts)):
            if list_of_gifts[index] == current_gift:
                list_of_gifts[index] = 'None'
    elif current_command_list[0] == 'Required':
        if 0 <= int(current_command_list[2]) < len(list_of_gifts):
            list_of_gifts[int(current_command_list[2])] = current_gift
    elif current_command_list[0] == 'JustInCase':
        list_of_gifts[-1] = current_gift
    command = input()
for gift in list_of_gifts:
    if not gift == 'None':
        print(f'{gift}', end=' ')
