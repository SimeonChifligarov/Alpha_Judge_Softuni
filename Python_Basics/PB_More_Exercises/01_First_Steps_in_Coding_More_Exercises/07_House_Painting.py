x = float(input())
y = float(input())
h = float(input())

front_wall_area = (x * x) - (1.2 * 2)
back_wall_area = x * x
side_walls_area = 2 * (x * y - 1.5 * 1.5)

total_wall_area = front_wall_area + back_wall_area + side_walls_area

green_paint_needed = total_wall_area / 3.4

roof_area = 2 * (x * y) + 2 * (0.5 * x * h)

red_paint_needed = roof_area / 4.3

print(f'{green_paint_needed:.2f}')
print(f'{red_paint_needed:.2f}')
