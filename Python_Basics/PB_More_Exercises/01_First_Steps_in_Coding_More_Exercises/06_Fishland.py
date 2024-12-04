mackerel_price = float(input())
sardine_price = float(input())
mackerel_kg = float(input())
sardine_kg = float(input())
mussels_kg = int(input())

palamud_price = mackerel_price * 1.60
safrid_price = sardine_price * 1.80
mussels_price = 7.50

total_cost = (
        palamud_price * mackerel_kg
        + safrid_price * sardine_kg
        + mussels_price * mussels_kg
)

print(f'{total_cost:.2f}')
