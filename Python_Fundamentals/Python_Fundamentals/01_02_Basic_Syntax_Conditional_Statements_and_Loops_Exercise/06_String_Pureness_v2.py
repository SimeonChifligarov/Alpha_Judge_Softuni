def check_purity(strings):
    results = []
    for string in strings:
        if ',' in string or '.' in string or '_' in string:
            results.append(f'{string} is not pure!')
        else:
            results.append(f'{string} is pure.')
    return results


if __name__ == '__main__':
    n = int(input())
    strings_input = [input() for _ in range(n)]

    outputs = check_purity(strings=strings_input)
    print('\n'.join(outputs))
