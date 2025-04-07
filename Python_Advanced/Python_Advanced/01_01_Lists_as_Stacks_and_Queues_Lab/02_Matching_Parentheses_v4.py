def extract_parentheses_groups(expression: str) -> list[str]:
    """
    Extracts and returns all groups enclosed in parentheses from an algebraic expression.

    Args:
        expression (str): The algebraic expression containing parentheses.

    Returns:
        list[str]: A list of substrings, each representing a set of parentheses and its contents.
    """
    stack = []
    groups = []
    for index, char in enumerate(expression):
        if char == '(':
            stack.append(index)
        elif char == ')':
            start_index = stack.pop()
            groups.append(expression[start_index:index + 1])
    return groups


if __name__ == '__main__':
    algebraic_expression = input()
    extracted_groups = extract_parentheses_groups(expression=algebraic_expression)
    print('\n'.join(extracted_groups))
