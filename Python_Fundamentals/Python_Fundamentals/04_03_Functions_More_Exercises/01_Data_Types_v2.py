def process_data(data_type: str, data_value: str) -> str:
    """Processes the input data based on its type and returns the formatted result."""
    if data_type == 'int':
        return str(int(data_value) * 2)
    elif data_type == 'real':
        return f'{float(data_value) * 1.5:.2f}'
    elif data_type == 'string':
        return f'${data_value}$'
    else:
        raise ValueError('Invalid data type provided.')


def main() -> None:
    data_type = input().strip()
    data_value = input().strip()
    try:
        print(process_data(data_type, data_value))
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
