def math_operations(*numbers: float, **operations: float) -> str:
    """
    This function applies math operations on numbers and updates values.

    Args:
        numbers: A bunch of floats to use
        operations: Keys 'a', 's', 'd', 'm' with initial numbers

    Returns:
        A string showing updated values sorted by value descending and key ascending
    """
    keys = ['a', 's', 'd', 'm']
    index = 0
    while index < len(numbers):
        current_key = keys[index % 4]
        current_value = numbers[index]
        if current_key == 'a':
            operations['a'] += current_value
        elif current_key == 's':
            operations['s'] -= current_value
        elif current_key == 'd':
            if current_value != 0:
                operations['d'] /= current_value
        elif current_key == 'm':
            operations['m'] *= current_value
        index += 1
    sorted_result = sorted(operations.items(), key=lambda x: (-x[1], x[0]))
    return '\n'.join([f'{key}: {value:.1f}' for key, value in sorted_result])


if __name__ == '__main__':
    output = math_operations(
        2.5, 3.0, 0.5, 4.0, 5.0,
        a=0,
        s=0,
        d=1,
        m=1
    )
    print(output)
