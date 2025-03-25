def check_ticket(ticket: str, winning_symbols: list[str]) -> str:
    """Checks if the given `ticket` is a jackpot, winning ticket, or no match."""
    if len(ticket) != 20:
        return 'invalid ticket'

    for sym in winning_symbols:
        if ticket.count(sym) == 20:
            return f'ticket "{ticket}" - 10{sym} Jackpot!'

    left_side = ticket[:10]
    right_side = ticket[10:]

    for sym in winning_symbols:
        for i in range(9, 5, -1):
            if sym * i in left_side and sym * i in right_side:
                return f'ticket "{ticket}" - {i}{sym}'

    return f'ticket "{ticket}" - no match'


if __name__ == '__main__':
    tickets_input: list[str] = [el.strip() for el in input().split(', ')]
    winning_symbols = ['@', '#', '$', '^']

    for ticket in tickets_input:
        print(check_ticket(ticket, winning_symbols))
