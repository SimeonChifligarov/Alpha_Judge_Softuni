def trapezoid_area(b1, b2, h):
    return (b1 + b2) * h / 2


base1 = float(input())
base2 = float(input())
height = float(input())

area = trapezoid_area(base1, base2, height)

print(f'{area:.2f}')
