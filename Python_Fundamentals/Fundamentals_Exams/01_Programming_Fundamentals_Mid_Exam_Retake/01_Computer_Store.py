total_without = 0.0
customer = None

while True:
    s = input()
    if s in ("special", "regular"):
        customer = s
        break
    price = float(s)
    if price <= 0:
        print("Invalid price!")
        continue
    total_without += price
if total_without == 0:
    print("Invalid order!")
else:
    taxes = total_without * 0.20
    total = total_without + taxes
    if customer == "special":
        total *= 0.90
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_without:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total:.2f}$")
