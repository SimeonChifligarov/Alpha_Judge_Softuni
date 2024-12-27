def birthday_party(guest_count, cover_price_per_person, budget):
    if 10 <= guest_count <= 15:
        cover_price_per_person *= 0.85
    elif 15 < guest_count <= 20:
        cover_price_per_person *= 0.80
    elif guest_count > 20:
        cover_price_per_person *= 0.75

    total_cover_cost = guest_count * cover_price_per_person
    cake_cost = budget * 0.10
    total_cost = total_cover_cost + cake_cost

    if budget >= total_cost:
        remaining_money = budget - total_cost
        return f'It is party time! {remaining_money:.2f} leva left.'
    else:
        needed_money = total_cost - budget
        return f'No party! {needed_money:.2f} leva needed.'


guest_num = int(input())
cover_price = float(input())
current_budget = float(input())

print(birthday_party(guest_count=guest_num, cover_price_per_person=cover_price, budget=current_budget))
