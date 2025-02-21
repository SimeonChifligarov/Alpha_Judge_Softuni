def generate_loading_bar(progress: int) -> str:
    completed = progress // 10
    return f'[{"%" * completed}{"." * (10 - completed)}]'


def display_loading_status(progress: int) -> None:
    loading_bar = generate_loading_bar(progress)

    if progress == 100:
        print('100% Complete!')
        print(loading_bar)
    else:
        print(f'{progress}% {loading_bar}')
        print('Still loading...')


if __name__ == '__main__':
    number = int(input())
    display_loading_status(number)
