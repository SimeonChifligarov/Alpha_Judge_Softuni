def manage_train(wagon_count: int) -> list[int]:
    """
    Manages a train with the given number of wagons, executing commands to add, insert, or remove people.
    """
    train_list = [0] * wagon_count

    commands = {
        'add': lambda args: train_list.__setitem__(-1, train_list[-1] + int(args[0])),
        'insert': lambda args: train_list.__setitem__(int(args[0]), train_list[int(args[0])] + int(args[1])),
        'leave': lambda args: train_list.__setitem__(int(args[0]), train_list[int(args[0])] - int(args[1])),
    }

    while True:
        command = input()
        if command == 'End':
            break

        parts = command.split()
        action, arguments = parts[0], parts[1:]
        commands[action](arguments)

    return train_list


if __name__ == '__main__':
    wagon_count_input = int(input())
    final_train = manage_train(wagon_count=wagon_count_input)
    print(final_train)
