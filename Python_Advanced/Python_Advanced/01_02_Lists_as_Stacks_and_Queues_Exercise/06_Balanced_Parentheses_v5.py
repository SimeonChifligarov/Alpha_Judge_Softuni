def crazy_balanced(s: str) -> str:
    """
    Sees if all the brackets are matched properly.

    Args:
        s: A string made only of brackets.

    Returns:
        'YES' if brackets match, 'NO' otherwise.
    """
    while any(x in s for x in ('()', '{}', '[]')):
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
    return 'YES' if not s else 'NO'


if __name__ == '__main__':
    brackets = input()
    answer = crazy_balanced(s=brackets)
    print(answer)
