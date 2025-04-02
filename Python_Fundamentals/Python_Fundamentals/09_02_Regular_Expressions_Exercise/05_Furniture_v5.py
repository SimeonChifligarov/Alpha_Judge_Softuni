import re


def calculate_total_cost(purchases: list[str]) -> tuple[list[str], float]:
    """
    Extracts valid furniture purchase data from the input list using regex,
    and calculates the total cost. Returns the list of furniture names and the total cost.
    """
    pattern = r'>>(?P<name>[a-zA-Z\s]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)'
    furniture = []
    total_cost = 0.0

    for line in purchases:
        match = re.match(pattern, line)
        if match:
            name = match.group('name')
            price = float(match.group('price'))
            quantity = int(match.group('quantity'))
            total_cost += price * quantity
            furniture.append(name)

    return furniture, total_cost


if __name__ == '__main__':
    input_lines = []

    while True:
        line = input().strip()
        if line == 'Purchase':
            break
        input_lines.append(line)

    bought_furniture, total_spent = calculate_total_cost(purchases=input_lines)

    print('Bought furniture:')
    for item in bought_furniture:
        print(item)
    print(f'Total money spend: {total_spent:.2f}')
