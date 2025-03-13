# If you receive a product, which already exists,
# increase its quantity by the input quantity and
# if its price is different, replace the price as well.

data = input()

products_dict = {}
while not data == 'buy':
    # split_data = data.split()
    # product = split_data[0]
    # price = float(split_data[1])
    # quantity = int(split_data[2])
    product, price, quantity = data.split()
    price, quantity = float(price), int(quantity)

    if product not in products_dict:
        products_dict[product] = {'Price': 0.0, 'Quantity': 0}
    products_dict[product]['Price'] = price
    products_dict[product]['Quantity'] += quantity
    data = input()

for prod, qty in products_dict.items():
    total_price = qty["Price"] * qty["Quantity"]
    print(f'{prod} -> {total_price:.2f}')
