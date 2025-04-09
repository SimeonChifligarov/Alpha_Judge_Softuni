from collections import deque
from typing import List


def serve_customers(food_available: int, orders_list: List[int]) -> List[str]:
    """
    Simulates serving customers based on available food and their orders.
    Returns the biggest order and the final state after attempting to serve all clients.
    """
    result = []
    orders = deque(orders_list)
    result.append(str(max(orders)))
    while orders:
        if food_available >= orders[0]:
            food_available -= orders.popleft()
        else:
            break
    if not orders:
        result.append('Orders complete')
    else:
        remaining_orders = ' '.join(str(order) for order in orders)
        result.append(f'Orders left: {remaining_orders}')
    return result


if __name__ == '__main__':
    food_input = int(input())
    orders_input = [int(el) for el in input().split()]
    output_result = serve_customers(food_available=food_input, orders_list=orders_input)
    for line in output_result:
        print(line)
