length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent_occupied = float(input())

volume_cm3 = length_cm * width_cm * height_cm
volume_liters = volume_cm3 / 1000
usable_volume = volume_liters * (1 - percent_occupied / 100)

print(f'{usable_volume:.3f}')
