def check_ticket(ticket: str) -> str:
    """Checks if a ticket is valid, winning, or a jackpot-winning ticket."""
    if len(ticket) != 20:
        return 'invalid ticket'

    winning_symbols = ('@', '#', '$', '^')  # '@#$^'

    left_half, right_half = ticket[:10], ticket[10:]

    for symbol in winning_symbols:
        for length in range(10, 5, -1):
            if symbol * length in left_half and symbol * length in right_half:
                if length == 10:
                    return f'ticket "{ticket}" - {length}{symbol} Jackpot!'
                return f'ticket "{ticket}" - {length}{symbol}'

    return f'ticket "{ticket}" - no match'


def process_tickets(text: str) -> list[str]:
    """Processes multiple tickets and returns their evaluation results."""
    tickets = [ticket.strip() for ticket in text.split(', ')]
    return [check_ticket(ticket) for ticket in tickets]


if __name__ == '__main__':
    input_text = input()

    results = process_tickets(text=input_text)
    for result in results:
        print(result)
