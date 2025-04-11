from collections import deque
from datetime import datetime, timedelta

data = input().split(';')
time = datetime.strptime(input(), '%H:%M:%S')

robots = []
available_robots = deque()

for el in data:
    robot_data = el.split('-')
    robot = {'name': robot_data[0], 'processing_time': int(robot_data[1]), 'available_at': time}
    robots.append(robot)

products = deque()
product = input()
while product != 'End':
    products.append(product)
    product = input()

time = time + timedelta(seconds=1)

while products:
    # Before anything: free any robots that are available
    for robot in robots:
        if time >= robot['available_at'] and robot not in available_robots:
            available_robots.append(robot)

    if available_robots:
        current_product = products.popleft()
        current_robot = available_robots.popleft()
        current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
        print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    else:
        # No robots free, but product must wait in line
        current_product = products.popleft()
        products.append(current_product)

    time = time + timedelta(seconds=1)
