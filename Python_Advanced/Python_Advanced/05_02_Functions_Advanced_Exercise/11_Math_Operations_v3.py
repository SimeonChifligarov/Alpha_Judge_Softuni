def math_operations(*values: float, **symbols: float) -> str:
    """
    This function does math operations on numbers and sorts the results.

    Args:
        values: A list of floats
        symbols: Four operations with initial values

    Returns:
        A string with results sorted nicely
    """
    action_order = ['a', 's', 'd', 'm']
    for idx, number in enumerate(values):
        current = action_order[idx % 4]
        if current == 'a':
            symbols['a'] += number
        elif current == 's':
            symbols['s'] -= number
        elif current == 'd':
            if number != 0:
                symbols['d'] /= number
        elif current == 'm':
            symbols['m'] *= number
    final_result = sorted(symbols.items(), key=lambda item: (-item[1], item[0]))
    output = [f'{letter}: {num:.1f}' for letter, num in final_result]
    return '\n'.join(output)


if __name__ == '__main__':
    starting_symbols = {
        'a': 0,
        's': 0,
        'd': 1,
        'm': 1
    }
    input_values = (2.5, 3.0, 0.5, 4.0, 5.0)
    print(math_operations(*input_values, **starting_symbols))
