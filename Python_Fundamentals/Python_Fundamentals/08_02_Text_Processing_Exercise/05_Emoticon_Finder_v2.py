string = input()

for index in range(len(string) - 1):
    if string[index] == ':':
        print(f'{string[index]}{string[index + 1]}')
