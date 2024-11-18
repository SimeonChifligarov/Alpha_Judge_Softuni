nylon_price_per_m2 = 1.50
paint_price_per_liter = 14.50
thinner_price_per_liter = 5.00
bags_cost = 0.40

additional_nylon = 2
additional_paint_percentage = 0.10
workers_percentage = 0.30

nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours_worked = int(input())

nylon_needed += additional_nylon
paint_needed += paint_needed * additional_paint_percentage

nylon_cost = nylon_needed * nylon_price_per_m2
paint_cost = paint_needed * paint_price_per_liter
thinner_cost = thinner_needed * thinner_price_per_liter

materials_total = nylon_cost + paint_cost + thinner_cost + bags_cost
workers_cost_per_hour = materials_total * workers_percentage
workers_cost = workers_cost_per_hour * hours_worked

total_cost = materials_total + workers_cost

print(total_cost)
