def get_sorted_todo_list() -> list[str]:
    """
    Receives to-do notes in the format '{importance}-{note}' until 'End' is entered.
    Returns a list of notes sorted by importance in ascending order.
    """
    todo_list = []

    while True:
        note = input()
        if note == 'End':
            break
        importance, task = note.split('-', maxsplit=1)
        todo_list.append((int(importance), task))

    return [task for _, task in sorted(todo_list)]


if __name__ == '__main__':
    sorted_todo_list = get_sorted_todo_list()
    print(sorted_todo_list)
