def manage_train(wagon_count: int) -> list[int]:
    """
    Manages a train with the given number of wagons, executing commands to add, insert, or remove people.
    """
    train_list = [0] * wagon_count

    while True:
        command = input()
        if command == 'End':
            break
        parts = command.split()
        action = parts[0]

        if action == 'add':
            train_list[-1] += int(parts[1])
        elif action == 'insert':
            train_list[int(parts[1])] += int(parts[2])
        elif action == 'leave':
            train_list[int(parts[1])] -= int(parts[2])

    return train_list


if __name__ == '__main__':
    wagon_count_input = int(input())
    final_train = manage_train(wagon_count=wagon_count_input)
    print(final_train)
