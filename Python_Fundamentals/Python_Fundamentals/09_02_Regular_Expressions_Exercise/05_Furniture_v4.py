import re


def calculate_total_cost() -> None:
    """
    Reads furniture purchase information, extracts valid data using regex,
    and calculates the total cost, printing the results.
    """
    pattern = r'>>(?P<name>[a-zA-Z\s]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)'
    furniture = []
    total_cost = 0.0

    while True:
        line = input().strip()
        if line == 'Purchase':
            break

        match = re.match(pattern, line)
        if match:
            name = match.group('name')
            price = float(match.group('price'))
            quantity = int(match.group('quantity'))
            total_cost += price * quantity
            furniture.append(name)

    print('Bought furniture:')
    for item in furniture:
        print(item)
    print(f'Total money spend: {total_cost:.2f}')


if __name__ == '__main__':
    calculate_total_cost()
