from collections import deque
from datetime import datetime, timedelta


def simulate_robots_work(robots_input: str, start: str, products_input: list[str]) -> None:
    """
    Simulates the robot assembly line with processing times.

    Args:
        robots_input: Robots with their times in one string.
        start: The start time as a string.
        products_input: A list of products arriving.

    Returns:
        Nothing, just prints logs of the work.
    """
    robots_info = {}
    busy_until = {}
    robots = robots_input.split(';')
    for r in robots:
        name, time_needed = r.split('-')
        robots_info[name] = int(time_needed)
        busy_until[name] = 0
    time_now = datetime.strptime(start, '%H:%M:%S')
    products = deque(products_input)
    time_passed = 0
    while products:
        time_now += timedelta(seconds=1)
        time_passed += 1
        product = products.popleft()
        available = False
        for robot_name in robots_info:
            if busy_until[robot_name] <= time_passed:
                busy_until[robot_name] = time_passed + robots_info[robot_name]
                print(f'{robot_name} - {product} [{time_now.strftime("%H:%M:%S")}]')
                available = True
                break
        if not available:
            products.append(product)


if __name__ == '__main__':
    robots_data = input()
    start_time = input()
    products_list = []
    while True:
        product_item = input()
        if product_item == 'End':
            break
        products_list.append(product_item)
    simulate_robots_work(robots_input=robots_data, start=start_time, products_input=products_list)
