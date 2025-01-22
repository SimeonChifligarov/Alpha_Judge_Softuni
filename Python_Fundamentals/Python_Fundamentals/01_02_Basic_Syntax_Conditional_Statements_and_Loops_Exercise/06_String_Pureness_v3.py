def check_purity(strings_to_check):
    forbidden_symbols = [',', '.', '_']
    results_list = []
    for item in strings_to_check:
        if any(symbol in item for symbol in forbidden_symbols):
            results_list.append(f'{item} is not pure!')
        else:
            results_list.append(f'{item} is pure.')
    return results_list


if __name__ == '__main__':
    number_of_strings = int(input())
    strings_input = [input() for _ in range(number_of_strings)]

    outputs_to_print = check_purity(strings_to_check=strings_input)
    
    for result in outputs_to_print:
        print(result)
