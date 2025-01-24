def calculate_christmas_expenses(quantity, days):
    ornament_price, ornament_points = 2, 5
    skirt_price, skirt_points = 5, 3
    garland_price, garland_points = 3, 10
    lights_price, lights_points = 15, 17

    total_cost = 0
    total_spirit = 0

    for day in range(1, days + 1):
        if day % 11 == 0:
            quantity += 2

        if day % 2 == 0:
            total_cost += quantity * ornament_price
            total_spirit += ornament_points

        if day % 3 == 0:
            total_cost += quantity * skirt_price
            total_cost += quantity * garland_price
            total_spirit += skirt_points + garland_points

        if day % 5 == 0:
            total_cost += quantity * lights_price
            total_spirit += lights_points
            if day % 3 == 0:
                total_spirit += 30

        if day % 10 == 0:
            total_spirit -= 20
            total_cost += skirt_price + garland_price + lights_price
            if day == days:
                total_spirit -= 30

    return total_cost, total_spirit


if __name__ == '__main__':
    decoration_quantity = int(input())
    remaining_days = int(input())
    cost, spirit = calculate_christmas_expenses(quantity=decoration_quantity, days=remaining_days)
    print(f'Total cost: {cost}')
    print(f'Total spirit: {spirit}')
