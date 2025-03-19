def reverse_strings():
    while True:
        data = input().strip()
        if data.lower() == 'end':
            break

        # print(f'{data} = {data[::-1]}')
        reversed_data = data[::-1]
        print(f'{data} = {reversed_data}')


if __name__ == '__main__':
    reverse_strings()
