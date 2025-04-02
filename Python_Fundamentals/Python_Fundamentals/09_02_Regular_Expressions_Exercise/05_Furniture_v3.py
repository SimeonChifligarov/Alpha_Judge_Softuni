import re


def extract_furniture_data() -> tuple[list[str], float]:
    """Extracts furniture names and calculates total price from input lines."""
    pattern = r'>>(?P<furniture>\w+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)'

    all_furniture = []
    total_price = 0.0

    while True:
        data_as_line = input().strip()
        if data_as_line == 'Purchase':
            break

        match = re.fullmatch(pattern, data_as_line)
        if match:
            all_furniture.append(match.group('furniture'))
            total_price += float(match.group('price')) * int(match.group('quantity'))

    return all_furniture, total_price


if __name__ == '__main__':
    furniture_list, total_spend = extract_furniture_data()

    print('Bought furniture:')
    if furniture_list:
        print('\n'.join(furniture_list))

    print(f'Total money spend: {total_spend:.2f}')
