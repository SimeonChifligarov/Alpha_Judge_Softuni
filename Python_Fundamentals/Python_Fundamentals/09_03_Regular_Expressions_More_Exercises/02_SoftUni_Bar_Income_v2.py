import re

ORDER_PATTERN = re.compile(r"""
    %(?P<name>[A-Z][a-z]+)%           # Customer name (Starts with capital, followed by lowercase)
    [^\|\$\.\%]*                      # Ignoring unnecessary characters
    <(?P<product>\w+)>                # Product name inside <>
    [^\|\$\.\%]*                      # Ignoring unnecessary characters
    \|(?P<count>\d+)\|                # Quantity of product
    [^\|\$\.\%0-9]*                   # Ignoring unnecessary characters
    (?P<price>\d+(\.\d+)?)\$          # Price (float or int) followed by $
""", re.VERBOSE)


def process_order(order_line: str) -> float:
    """Processes a single order line and returns the calculated price, or 0 if invalid."""
    match = ORDER_PATTERN.match(order_line)
    if match:
        data = match.groupdict()
        total = int(data['count']) * float(data['price'])
        print(f"{data['name']}: {data['product']} - {total:.2f}")
        return total
    return 0


def main():
    """Main function to handle input processing and calculate total income."""
    total_income = 0

    while True:
        order_line = input().strip()
        if order_line == 'end of shift':
            break
        total_income += process_order(order_line)

    print(f'Total income: {total_income:.2f}')


if __name__ == '__main__':
    main()
