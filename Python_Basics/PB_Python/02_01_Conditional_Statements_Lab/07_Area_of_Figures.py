figure = input()

area = 0
if figure == 'square':
    side = float(input())
    area = side ** 2
elif figure == 'rectangle':
    width = float(input())
    height = float(input())
    area = width * height
elif figure == 'circle':
    radius = float(input())
    area = 3.14159 * radius ** 2
elif figure == 'triangle':
    base = float(input())
    height = float(input())
    area = (base * height) / 2

if area <= 0:
    print('invalid input values')
    exit(5)

print(f'{area:.3f}')
