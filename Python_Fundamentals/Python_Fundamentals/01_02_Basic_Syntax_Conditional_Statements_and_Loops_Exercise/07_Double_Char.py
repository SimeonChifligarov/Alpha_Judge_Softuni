while True:
    string = input()
    if string == 'End':
        break

    if string == 'SoftUni':
        continue

    double_char_list = []
    for char in string:
        # double_char_list.append(f'{char}{char}')
        double_char_list.append(char * 2)

    print(''.join(double_char_list))
