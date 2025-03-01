def process_room(chairs: str, visitors: int, room_number: int) -> int:
    return len(chairs) - visitors


def handle_room_result(free_chairs: int, room_number: int) -> int:
    if free_chairs < 0:
        print(f'{abs(free_chairs)} more chairs needed in room {room_number}')
        return -1
    return free_chairs


def update_counters(result: int, fails: int, total_free_chairs: int) -> tuple[int, int]:
    if result == -1:
        fails += 1
    else:
        total_free_chairs += result
    return fails, total_free_chairs


def check_chairs(n: int) -> None:
    total_free_chairs = 0
    fails = 0

    for room in range(1, n + 1):
        chairs, visitors = input().split()
        free_chairs = process_room(chairs=chairs, visitors=int(visitors), room_number=room)
        result = handle_room_result(free_chairs=free_chairs, room_number=room)
        fails, total_free_chairs = update_counters(result=result, fails=fails, total_free_chairs=total_free_chairs)

    if fails == 0:
        print(f'Game On, {total_free_chairs} free chairs left')


if __name__ == '__main__':
    rooms_count = int(input())
    check_chairs(n=rooms_count)
