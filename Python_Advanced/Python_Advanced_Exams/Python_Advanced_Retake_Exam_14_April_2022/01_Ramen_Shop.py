from collections import deque

bowls = list(map(int, input().split(", ")))
customers = deque(map(int, input().split(", ")))

while bowls and customers:
    bowl = bowls[-1]
    customer = customers[0]
    if bowl == customer:
        bowls.pop()
        customers.popleft()
    elif bowl > customer:
        bowls[-1] = bowl - customer
        customers.popleft()
    else:
        customers.popleft()
        customers.appendleft(customer - bowl)
        bowls.pop()

if not customers:
    print("Great job! You served all the customers.")
    if bowls:
        print("Bowls of ramen left: " + ", ".join(map(str, bowls)))
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print("Customers left: " + ", ".join(map(str, customers)))
