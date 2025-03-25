tickets = [el.strip() for el in input().split(',')]

winning_symbols = ['@', '#', '$', '^']

for ticket in tickets:
    is_jackpot = False
    is_winning = False
    if not len(ticket) == 20:
        print('invalid ticket')
        continue
    for sym in winning_symbols:
        if ticket.count(sym) == 20:
            print(f'ticket "{ticket}" - 10{sym} Jackpot!')
            is_jackpot = True
    if not is_jackpot:
        left_side_ticket = ticket[:10]
        right_side_ticket = ticket[10:]
        for sym in winning_symbols:
            for i in range(9, 5, -1):
                if sym * i in left_side_ticket and sym * i in right_side_ticket:
                    print(f'ticket "{ticket}" - {i}{sym}')
                    is_winning = True
                    break

    if not is_jackpot and not is_winning:
        print(f'ticket "{ticket}" - no match')
