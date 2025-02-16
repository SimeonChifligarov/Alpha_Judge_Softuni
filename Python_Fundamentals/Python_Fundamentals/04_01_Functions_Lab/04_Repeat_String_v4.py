def repeat_string(text: str, count: int) -> str:
    """
    Returns a new string by repeating the given string a specified number of times.
    """
    result = text * count
    return result


if __name__ == '__main__':
    input_text = input()
    input_count = int(input())
    output = repeat_string(text=input_text, count=input_count)
    print(output)
