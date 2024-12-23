def calculate_ticket_price(stage, ticket_type, ticket_count, photo_option):
    prices = {
        'Quarter final':
            {
                'Standard': 55.50,
                'Premium': 105.20,
                'VIP': 118.90,
            },
        'Semi final':
            {
                'Standard': 75.88,
                'Premium': 125.22,
                'VIP': 300.40,
            },
        'Final':
            {
                'Standard': 110.10,
                'Premium': 160.66,
                'VIP': 400.00,
            },
    }

    ticket_price = prices[stage][ticket_type]
    total_price = ticket_price * ticket_count

    if total_price > 4000:
        total_price *= 0.75
        photo_option = 'N'
    elif total_price > 2500:
        total_price *= 0.90

    if photo_option == 'Y':
        total_price += 40 * ticket_count

    print(f'{total_price:.2f}')


c_stage = input()
c_ticket_type = input()
c_ticket_count = int(input())
c_photo_option = input()

calculate_ticket_price(stage=c_stage, ticket_type=c_ticket_type, ticket_count=c_ticket_count,
                       photo_option=c_photo_option)
