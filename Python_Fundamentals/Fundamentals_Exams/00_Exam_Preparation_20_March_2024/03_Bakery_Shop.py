stock = {}
sold = 0
while True:
    line = input()
    if line == "Complete":
        break
    parts = line.split()
    cmd = parts[0]
    qty = int(parts[1])
    food = parts[2]
    if cmd == "Receive":
        if qty > 0:
            stock[food] = stock.get(food, 0) + qty
    elif cmd == "Sell":
        if food not in stock:
            print(f"You do not have any {food}.")
        else:
            if stock[food] < qty:
                sold += stock[food]
                print(f"There aren't enough {food}. You sold the last {stock[food]} of them.")
                del stock[food]
            else:
                stock[food] -= qty
                sold += qty
                print(f"You sold {qty} {food}.")
                if stock[food] == 0:
                    del stock[food]

for f, q in stock.items():
    print(f"{f}: {q}")
print(f"All sold: {sold} goods")
