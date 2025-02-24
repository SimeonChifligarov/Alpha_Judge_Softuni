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
            people_count = int(parts[1])
            train_list[-1] += people_count
        elif action == 'insert':
            wagon_index = int(parts[1])
            people_count = int(parts[2])
            train_list[wagon_index] += people_count
        elif action == 'leave':
            wagon_index = int(parts[1])
            people_count = int(parts[2])
            train_list[wagon_index] -= people_count

    return train_list


if __name__ == '__main__':
    wagon_count_input = int(input())
    final_train = manage_train(wagon_count=wagon_count_input)
    print(final_train)
