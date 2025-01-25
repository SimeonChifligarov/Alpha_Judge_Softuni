def find_capital_indices(text):
    indices = [index for index, char in enumerate(text) if char.isupper()]
    return indices


if __name__ == '__main__':
    input_text = input()
    result = find_capital_indices(text=input_text)
    print(result)
