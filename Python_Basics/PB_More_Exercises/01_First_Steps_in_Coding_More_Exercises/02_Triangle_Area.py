def triangle_area(base, height):
    return base * height / 2


b = float(input())
h = float(input())

area = triangle_area(b, h)

print(f'{area:.2f}')
