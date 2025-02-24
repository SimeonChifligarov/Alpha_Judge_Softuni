def get_sorted_chores() -> list:
    """Receives and sorts to-do notes based on importance."""
    chores = [None] * 11  # Maximum importance is 10

    while True:
        to_do_chores = input()
        if to_do_chores == 'End':
            break

        importance, chore = to_do_chores.split('-', maxsplit=1)  # ensure the task part can contain dashes
        chores[int(importance)] = chore

    return [chore for chore in chores if chore is not None]


def main():
    sorted_chores = get_sorted_chores()
    print(sorted_chores)


if __name__ == '__main__':
    main()
