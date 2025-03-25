def is_valid_ticket(ticket: str) -> bool:
    """Checks if a ticket is valid (exactly 20 characters long)."""
    return len(ticket) == 20


def get_winning_match(ticket: str) -> tuple[int, str] | None:
    """Returns the winning symbol and length if a ticket is winning, else None."""
    winning_symbols = ('@', '#', '$', '^')  # '@#$^'
    left_half, right_half = ticket[:10], ticket[10:]

    for symbol in winning_symbols:
        for length in range(10, 5, -1):
            if symbol * length in left_half and symbol * length in right_half:
                return length, symbol
    return None


def format_ticket_result(ticket: str, match: tuple[int, str] | None) -> str:
    """Formats the ticket result message based on whether it's winning, jackpot, or no match."""
    if not is_valid_ticket(ticket):
        return 'invalid ticket'
    if match:
        length, symbol = match
        if length == 10:
            return f'ticket "{ticket}" - {length}{symbol} Jackpot!'
        return f'ticket "{ticket}" - {length}{symbol}'
    return f'ticket "{ticket}" - no match'


def process_tickets(text: str) -> list[str]:
    """Processes multiple tickets and returns their evaluation results."""
    tickets = [ticket.strip() for ticket in text.split(', ')]
    return [format_ticket_result(ticket, get_winning_match(ticket)) for ticket in tickets]


if __name__ == '__main__':
    input_text = input()
    results = process_tickets(text=input_text)
    for result in results:
        print(result)
