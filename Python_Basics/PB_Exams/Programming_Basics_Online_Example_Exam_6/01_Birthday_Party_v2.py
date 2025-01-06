def calculate_party_budget():
    hall_rent = float(input())
    
    cake_price = hall_rent * 0.20
    drinks_price = cake_price * 0.55
    animator_price = hall_rent / 3

    total_budget = hall_rent + cake_price + drinks_price + animator_price
    print(f'{total_budget:.2f}')


if __name__ == '__main__':
    calculate_party_budget()
