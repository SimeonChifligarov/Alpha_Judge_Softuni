def double_characters(strings_list):
    results_list = []
    for text in strings_list:
        if text != 'SoftUni':
            doubled_text = ''.join(char * 2 for char in text)
            results_list.append(doubled_text)
    return results_list


if __name__ == '__main__':
    inputs = []
    while True:
        current_input = input()
        if current_input == 'End':
            break
        inputs.append(current_input)
    outputs_to_print = double_characters(strings_list=inputs)
    for result in outputs_to_print:
        print(result)
