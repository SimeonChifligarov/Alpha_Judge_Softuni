def is_brackets_balanced(text: str) -> str:
    """
    Tells if the brackets in the text are balanced.

    Args:
        text: A string made of brackets only.

    Returns:
        'YES' if the brackets are fine, 'NO' if not.
    """
    pairs = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for char in text:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack.pop()] != char:
                return 'NO'
    return 'YES' if not stack else 'NO'


if __name__ == '__main__':
    input_text = input()
    result = is_brackets_balanced(text=input_text)
    print(result)
