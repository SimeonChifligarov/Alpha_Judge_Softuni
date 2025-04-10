def check_balanced_brackets(sequence: str) -> str:
    """
    Checks if the given sequence of brackets is balanced.

    Args:
        sequence: A string containing only brackets.

    Returns:
        'YES' if brackets are balanced, 'NO' otherwise.
    """
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    for symbol in sequence:
        if symbol in bracket_map.values():
            stack.append(symbol)
        elif symbol in bracket_map:
            if not stack or stack.pop() != bracket_map[symbol]:
                return 'NO'
    return 'YES' if not stack else 'NO'


if __name__ == '__main__':
    brackets_sequence = input()
    answer = check_balanced_brackets(sequence=brackets_sequence)
    print(answer)
