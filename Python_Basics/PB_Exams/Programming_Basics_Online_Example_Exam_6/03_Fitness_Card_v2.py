def fitness_card_budget(balance, gender, age, sport):
    prices = {
        'm': {'Gym': 42, 'Boxing': 41, 'Yoga': 45, 'Zumba': 34, 'Dances': 51, 'Pilates': 39},
        'f': {'Gym': 35, 'Boxing': 37, 'Yoga': 42, 'Zumba': 31, 'Dances': 53, 'Pilates': 37},
    }

    card_price = prices[gender][sport]

    if age <= 19:
        card_price *= 0.80

    if balance >= card_price:
        return f'You purchased a 1 month pass for {sport}.'
    else:
        needed_money = card_price - balance
        return f'You don\'t have enough money! You need ${needed_money:.2f} more.'


if __name__ == '__main__':
    available_money = float(input())
    client_gender = input()
    client_age = int(input())
    chosen_sport = input()
    output = fitness_card_budget(balance=available_money, gender=client_gender, age=client_age, sport=chosen_sport)
    print(output)
