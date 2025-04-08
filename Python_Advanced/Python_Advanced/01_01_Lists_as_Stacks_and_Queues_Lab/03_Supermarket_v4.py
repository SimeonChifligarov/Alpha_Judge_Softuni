from collections import deque


def manage_supermarket_queue() -> None:
    """
    Manages a supermarket queue based on input commands and customer names.
    Handles adding customers, serving them, and displaying queue status.
    """
    customers = deque()
    while True:
        action = input()
        if action == 'End':
            break

        elif action == 'Paid':
            print('\n'.join(customers))
            customers.clear()
        else:
            customers.append(action)

    print(f'{len(customers)} people remaining.')


if __name__ == '__main__':
    manage_supermarket_queue()
