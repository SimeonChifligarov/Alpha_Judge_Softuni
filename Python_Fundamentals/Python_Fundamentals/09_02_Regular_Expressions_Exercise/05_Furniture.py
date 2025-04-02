import re

pattern = r'>>(?P<furniture>\w+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)'

data_as_line = input()
all_furniture = []
total_price = 0

while not data_as_line == 'Purchase':
    current_furniture = re.fullmatch(pattern, data_as_line)
    if current_furniture:
        all_furniture.append(current_furniture['furniture'])
        total_price += float(current_furniture['price']) * int(current_furniture['quantity'])
    data_as_line = input()

print('Bought furniture:')
for furn in all_furniture:
    print(furn)
print(f'Total money spend: {total_price:.2f}')
