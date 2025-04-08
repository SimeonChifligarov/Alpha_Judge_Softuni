def manage_supermarket_queue() -> None:
    """
    Manages a supermarket queue based on input commands and customer names.
    Handles adding customers, serving them, and displaying queue status.
    """
    queue = []
    while True:
        command = input()
        if command == 'End':
            break

        if command == 'Paid':
            print('\n'.join(queue))
            queue.clear()
        else:
            queue.append(command)
    print(f'{len(queue)} people remaining.')


if __name__ == '__main__':
    manage_supermarket_queue()
