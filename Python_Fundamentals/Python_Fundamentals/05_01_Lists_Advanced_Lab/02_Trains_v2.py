def manage_train(number_of_wagons: int) -> None:
    """"Manages a train with wagons based on user commands."""
    wagons = [0] * number_of_wagons

    while True:
        command_full = input()
        if command_full == 'End':
            break

        command_parts = command_full.split()
        command = command_parts[0]

        if command == 'add':
            people = int(command_parts[1])
            wagons[-1] += people
        elif command == 'insert':
            index, people = int(command_parts[1]), int(command_parts[2])
            wagons[index] += people
        elif command == 'leave':
            index, people = int(command_parts[1]), int(command_parts[2])
            wagons[index] -= people

    print(wagons)


def main():
    number_of_wagons = int(input())
    manage_train(number_of_wagons)


if __name__ == '__main__':
    main()
