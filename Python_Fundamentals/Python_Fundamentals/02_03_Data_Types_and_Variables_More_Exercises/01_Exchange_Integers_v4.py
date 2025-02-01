def exchange_values(a: int, b: int) -> None:
    print('Before:')
    print(f'a = {a}')
    print(f'b = {b}')
    a, b = b, a
    print('After:')
    print(f'a = {a}')
    print(f'b = {b}')


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    exchange_values(a=x, b=y)
