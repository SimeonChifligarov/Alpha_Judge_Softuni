from collections import deque

orders = deque(int(x) for x in input().split(", "))
employees = [int(x) for x in input().split(", ")]

total = 0

while orders and employees:
    while orders and (orders[0] <= 0 or orders[0] > 10):
        orders.popleft()
    if not orders:
        break
    order = orders[0]
    emp = employees[-1]
    made = min(emp, order)
    total += made
    if emp >= order:
        orders.popleft()
        employees.pop()
    else:
        orders[0] = order - emp
        employees.pop()

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total}")
    if employees:
        print("Employees: " + ", ".join(map(str, employees)))
else:
    print("Not all orders are completed.")
    print("Orders left: " + ", ".join(map(str, orders)))
