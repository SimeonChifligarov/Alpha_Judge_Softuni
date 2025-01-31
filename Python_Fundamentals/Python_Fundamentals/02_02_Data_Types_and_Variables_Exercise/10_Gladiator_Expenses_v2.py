def calculate_gladiator_expenses(lost_fights: int, helmet_cost: float, sword_cost: float, shield_cost: float,
                                 armor_cost: float) -> str:
    total_expenses = 0
    shield_break_count = 0

    for fight in range(1, lost_fights + 1):
        if fight % 2 == 0:
            total_expenses += helmet_cost
        if fight % 3 == 0:
            total_expenses += sword_cost
        if fight % 2 == 0 and fight % 3 == 0:
            total_expenses += shield_cost
            shield_break_count += 1
            if shield_break_count % 2 == 0:
                total_expenses += armor_cost

    return f'Gladiator expenses: {total_expenses:.2f} aureus'


if __name__ == '__main__':
    lost_fights_input = int(input())
    helmet_price_input = float(input())
    sword_price_input = float(input())
    shield_price_input = float(input())
    armor_price_input = float(input())

    result = calculate_gladiator_expenses(
        lost_fights=lost_fights_input,
        helmet_cost=helmet_price_input,
        sword_cost=sword_price_input,
        shield_cost=shield_price_input,
        armor_cost=armor_price_input,
    )
    print(result)
