def process_input(data_type: str, value: str) -> str:
    """
    Processes the input based on its type.

    :param data_type: The type of data ('int', 'real', or 'string').
    :param value: The value to be processed.
    :return: The processed result as a string.
    """
    if data_type == 'int':
        return str(int(value) * 2)
    elif data_type == 'real':
        return f'{float(value) * 1.5:.2f}'
    elif data_type == 'string':
        return f'${value}$'
    return ''


if __name__ == '__main__':
    type_input = input()
    value_input = input()
    result = process_input(data_type=type_input, value=value_input)
    print(result)
