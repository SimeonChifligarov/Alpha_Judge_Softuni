from collections import deque
from typing import List


def manage_orders(total_food: int, client_orders: List[int]) -> List[str]:
    """
    Manages serving customers based on available food and their order demands.
    Returns the biggest single order and the service result.
    """
    result_output = []
    orders_queue = deque(client_orders)
    biggest_order = max(order for order in orders_queue)
    result_output.append(str(biggest_order))
    while orders_queue and total_food >= orders_queue[0]:
        total_food -= orders_queue.popleft()
    if not orders_queue:
        result_output.append('Orders complete')
    else:
        pending_orders = ' '.join(str(order) for order in orders_queue)
        result_output.append(f'Orders left: {pending_orders}')
    return result_output


if __name__ == '__main__':
    total_food_input = int(input())
    client_orders_input = [int(el) for el in input().split()]
    service_result_output = manage_orders(total_food=total_food_input, client_orders=client_orders_input)
    for output_line in service_result_output:
        print(output_line)
