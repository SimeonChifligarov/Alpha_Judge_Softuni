def loading_bar(num):
    num_dev_by_ten = num // 10
    loading_process = ['.'] * 10
    for index in range(num_dev_by_ten):
        loading_process[index] = '%'
    if num_dev_by_ten == 10:
        print('100% Complete!')
        print(f'[{"".join(loading_process)}]')
    else:
        print(f'{num}% [{"".join(loading_process)}]')
        print('Still loading...')


number = int(input())
loading_bar(number)
