def calculate_egg_sales(size, color, batches_count):
    price_chart = {
        'Large': {'Red': 16, 'Green': 12, 'Yellow': 9},
        'Medium': {'Red': 13, 'Green': 9, 'Yellow': 7},
        'Small': {'Red': 9, 'Green': 8, 'Yellow': 5},
    }

    price_per_batch = price_chart[size][color]
    total_income = price_per_batch * batches_count
    net_income = total_income * 0.65
    return f'{net_income:.2f} leva.'


size_input = input()
color_input = input()
batches_input = int(input())

print(calculate_egg_sales(size_input, color_input, batches_input))
