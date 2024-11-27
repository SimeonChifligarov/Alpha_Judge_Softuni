# using while True

max_number = None

while True:
    command = input()
    if command == 'Stop':
        break

    number = int(command)
    if max_number is None or number > max_number:
        max_number = number

print(max_number)
