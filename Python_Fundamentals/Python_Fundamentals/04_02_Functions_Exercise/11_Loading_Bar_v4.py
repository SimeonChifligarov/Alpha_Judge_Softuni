def loading_bar(progress: int) -> str:
    """
    Returns a loading bar representation based on the given progress percentage.
    """
    bar = '[' + '%' * (progress // 10) + '.' * (10 - progress // 10) + ']'
    if progress == 100:
        return '100% Complete!\n' + bar
    return f'{progress}% {bar}\nStill loading...'


if __name__ == '__main__':
    input_progress = int(input())
    result = loading_bar(progress=input_progress)
    print(result)
