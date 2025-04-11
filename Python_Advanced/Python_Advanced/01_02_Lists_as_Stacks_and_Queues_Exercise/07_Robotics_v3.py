from collections import deque
from datetime import datetime, timedelta

def fixed_process_factory(robots_line: str, starting_time: str, items: list[str]) -> None:
    """
    Runs the factory where robots work on products one by one.

    Args:
        robots_line: A string with all robots and their times.
        starting_time: The clock time when robots start.
        items: A list of products that arrive.

    Returns:
        Nothing, just prints the working robots.
    """
    robots = []
    busy_until = {}
    for part in robots_line.split(';'):
        robot, seconds = part.split('-')
        robots.append((robot, int(seconds)))
        busy_until[robot] = 0
    clock = datetime.strptime(starting_time, '%H:%M:%S')
    products = deque(items)
    seconds_passed = 0
    while products:
        clock += timedelta(seconds=1)
        seconds_passed += 1
        product = products.popleft()
        assigned = False
        for robot_name, process_time in robots:
            if busy_until[robot_name] <= seconds_passed:
                busy_until[robot_name] = seconds_passed + process_time
                print(f'{robot_name} - {product} [{clock.strftime("%H:%M:%S")}]')
                assigned = True
                break
        if not assigned:
            products.append(product)

if __name__ == '__main__':
    robots_line_input = input()
    starting_time_input = input()
    products_input = []
    while True:
        item = input()
        if item == 'End':
            break
        products_input.append(item)
    fixed_process_factory(robots_line=robots_line_input, starting_time=starting_time_input, items=products_input)
