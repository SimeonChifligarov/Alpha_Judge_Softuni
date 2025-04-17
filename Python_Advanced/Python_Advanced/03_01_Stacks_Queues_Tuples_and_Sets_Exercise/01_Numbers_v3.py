def process_numbers(collection_1: set[int], collection_2: set[int], total_actions: int) -> None:
    """
    This function changes two sets of numbers. It can add, remove or check subsets.

    Args:
        collection_1 (set[int]): The first collection of numbers.
        collection_2 (set[int]): The second collection of numbers.
        total_actions (int): How many actions to do.

    Returns:
        None
    """
    actions = [input().split() for _ in range(total_actions)]
    for act in actions:
        if act[0] == 'Add' and act[1] == 'First':
            collection_1 |= {int(x) for x in act[2:]}
        elif act[0] == 'Add' and act[1] == 'Second':
            collection_2 |= {int(x) for x in act[2:]}
        elif act[0] == 'Remove' and act[1] == 'First':
            collection_1 -= {int(x) for x in act[2:]}
        elif act[0] == 'Remove' and act[1] == 'Second':
            collection_2 -= {int(x) for x in act[2:]}
        elif act[0] == 'Check' and act[1] == 'Subset':
            print('True' if collection_1 <= collection_2 or collection_2 <= collection_1 else 'False')
    print(', '.join([str(num) for num in sorted(collection_1)]))
    print(', '.join([str(num) for num in sorted(collection_2)]))


if __name__ == '__main__':
    group_1_input = {int(x) for x in input().split()}
    group_2_input = {int(x) for x in input().split()}
    commands_input = int(input())
    process_numbers(collection_1=group_1_input, collection_2=group_2_input, total_actions=commands_input)
