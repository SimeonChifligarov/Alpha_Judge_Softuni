def manage_sequences(seq_1: set[int], seq_2: set[int], num_commands: int) -> None:
    """
    This function manages two sets of numbers. It can add, remove numbers or check subsets.

    Args:
        seq_1 (set[int]): The first set of numbers.
        seq_2 (set[int]): The second set of numbers.
        num_commands (int): Number of commands to process.

    Returns:
        None
    """
    for _ in range(num_commands):
        command_parts = input().split()
        action = command_parts[0]
        target = command_parts[1]
        if action == 'Add':
            numbers_to_add = {int(el) for el in command_parts[2:]}
            if target == 'First':
                seq_1.update(numbers_to_add)
            elif target == 'Second':
                seq_2.update(numbers_to_add)
        elif action == 'Remove':
            numbers_to_remove = {int(el) for el in command_parts[2:]}
            if target == 'First':
                seq_1.difference_update(numbers_to_remove)
            elif target == 'Second':
                seq_2.difference_update(numbers_to_remove)
        elif action == 'Check' and target == 'Subset':
            if seq_1.issubset(seq_2) or seq_2.issubset(seq_1):
                print('True')
            else:
                print('False')
    print(', '.join(str(el) for el in sorted(seq_1)))
    print(', '.join(str(el) for el in sorted(seq_2)))


if __name__ == '__main__':
    sequence_1_input = {int(el) for el in input().split()}
    sequence_2_input = {int(el) for el in input().split()}
    number_of_commands_input = int(input())
    manage_sequences(seq_1=sequence_1_input, seq_2=sequence_2_input, num_commands=number_of_commands_input)
