def calculate_total_expenses(annual_fee):
    sneakers_price = annual_fee * 0.6
    outfit_price = sneakers_price * 0.8
    ball_price = outfit_price / 4
    accessories_price = ball_price / 5
    
    return annual_fee + sneakers_price + outfit_price + ball_price + accessories_price


def main():
    annual_fee = int(input())
    total_expenses = calculate_total_expenses(annual_fee)
    print(f'{total_expenses:.2f}')


if __name__ == '__main__':
    main()
