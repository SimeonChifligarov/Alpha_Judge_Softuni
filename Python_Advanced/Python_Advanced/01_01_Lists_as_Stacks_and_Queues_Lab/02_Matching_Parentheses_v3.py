def extract_parentheses_groups(expression: str) -> str:
    """
    Extracts and returns all groups enclosed in parentheses from an algebraic expression as a joined string.

    Args:
        expression (str): The algebraic expression containing parentheses.

    Returns:
        str: A single string where each parentheses group is separated by a newline character.
    """
    stack = []
    groups = []
    for index, char in enumerate(expression):
        if char == '(':
            stack.append(index)
        elif char == ')':
            start_index = stack.pop()
            groups.append(expression[start_index:index + 1])
    return '\n'.join(groups)


if __name__ == '__main__':
    algebraic_expression = input()
    extracted_groups = extract_parentheses_groups(expression=algebraic_expression)
    print(extracted_groups)
