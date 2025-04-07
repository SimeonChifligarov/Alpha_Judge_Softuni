def reverse_string_using_stack(text: str) -> str:
    """
    Reverses a given string using a stack approach.

    Args:
        text (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    stack = [char for char in text]
    reversed_text = ''.join(stack.pop() for _ in range(len(stack)))
    return reversed_text


if __name__ == '__main__':
    input_text = input()
    result = reverse_string_using_stack(text=input_text)
    print(result)
