def calculate_agency_profit(company_name, adult_tickets, child_tickets, adult_ticket_price, service_fee):
    child_ticket_price = adult_ticket_price * 0.3
    total_adult = (adult_ticket_price + service_fee) * adult_tickets
    total_child = (child_ticket_price + service_fee) * child_tickets
    total_price = total_adult + total_child
    profit = total_price * 0.2
    return f'The profit of your agency from {company_name} tickets is {profit:.2f} lv.'


if __name__ == '__main__':
    company_name_input = input()
    adult_tickets_input = int(input())
    child_tickets_input = int(input())
    adult_ticket_price_input = float(input())
    service_fee_input = float(input())

    result = calculate_agency_profit(
        company_name=company_name_input,
        adult_tickets=adult_tickets_input,
        child_tickets=child_tickets_input,
        adult_ticket_price=adult_ticket_price_input,
        service_fee=service_fee_input
    )
    print(result)
