def calculate_workplaces(width, height):
    width_cm = width * 100
    height_cm = height * 100 - 100
    desks_per_row = height_cm // 70
    rows = width_cm // 120
    total_places = desks_per_row * rows
    usable_places = total_places - 3
    return int(usable_places)


w = float(input())
h = float(input())

workplaces = calculate_workplaces(w, h)
print(workplaces)
