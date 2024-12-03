def calculate_revenue(price_veg, price_fruit, kg_veg, kg_fruit):
    total_lv = (price_veg * kg_veg) + (price_fruit * kg_fruit)
    total_eur = total_lv / 1.94
    return total_eur


vegetable_price = float(input())
fruit_price = float(input())
vegetable_weight = int(input())
fruit_weight = int(input())


revenue = calculate_revenue(vegetable_price, fruit_price, vegetable_weight, fruit_weight)
print(f'{revenue:.2f}')
