from collections import deque


def key_revolver_mission(bullet_price: int, barrel_capacity: int, bullets_list: list[int], locks_list: list[int],
                         intelligence_value: int) -> None:
    """
    This function helps Sam unlock the safe.
    It shows if he succeeded and how much money he earned.

    Args:
        bullet_price: Price of one bullet.
        barrel_capacity: Number of bullets gun can hold.
        bullets_list: Sizes of bullets.
        locks_list: Sizes of locks.
        intelligence_value: Money earned after mission.

    Returns:
        None
    """
    bullets = bullets_list
    locks = deque(locks_list)
    barrel_loaded = barrel_capacity
    bullets_used = 0

    while bullets and locks:
        bullet = bullets.pop()
        lock = locks[0]
        bullets_used += 1
        barrel_loaded -= 1

        if bullet <= lock:
            print('Bang!')
            locks.popleft()
        else:
            print('Ping!')

        if barrel_loaded == 0 and bullets:
            print('Reloading!')
            barrel_loaded = barrel_capacity

    if not locks:
        money_earned = intelligence_value - (bullets_used * bullet_price)
        print(f'{len(bullets)} bullets left. Earned ${money_earned}')
    else:
        print(f"Couldn't get through. Locks left: {len(locks)}")


if __name__ == '__main__':
    bullet_cost_input = int(input())
    gun_barrel_input = int(input())
    bullets_input = [int(el) for el in input().split()]
    locks_input = [int(el) for el in input().split()]
    intelligence_value_input = int(input())

    key_revolver_mission(
        bullet_price=bullet_cost_input,
        barrel_capacity=gun_barrel_input,
        bullets_list=bullets_input,
        locks_list=locks_input,
        intelligence_value=intelligence_value_input
    )
