def check_chairs(n: int) -> None:
    total_free_chairs = 0
    fails = 0

    for room in range(1, n + 1):
        chairs, visitors = input().split()
        free_chairs = len(chairs) - int(visitors)

        if free_chairs < 0:
            print(f'{abs(free_chairs)} more chairs needed in room {room}')
            fails += 1
        else:
            total_free_chairs += free_chairs

    if fails == 0:
        print(f'Game On, {total_free_chairs} free chairs left')


if __name__ == '__main__':
    rooms_count = int(input())
    check_chairs(n=rooms_count)
