import math


def paint_walls(height, width, unpainted_percent):
    total_area = 4 * height * width
    paintable_area = math.ceil(total_area * (1 - unpainted_percent / 100))
    paint_left = paintable_area

    while True:
        command = input()
        if command == 'Tired!':
            print(f'{paint_left} quadratic m left.')
            break
        paint_liters = int(command)
        paint_left -= paint_liters

        if paint_left <= 0:
            if paint_left < 0:
                print(f'All walls are painted and you have {abs(paint_left)} l paint left!')
            else:
                print('All walls are painted! Great job, Pesho!')
            break


wall_height = int(input())
wall_width = int(input())
unpainted_percentage_input = int(input())
paint_walls(height=wall_height, width=wall_width, unpainted_percent=unpainted_percentage_input)
