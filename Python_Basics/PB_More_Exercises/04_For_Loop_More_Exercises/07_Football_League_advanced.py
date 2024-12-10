stadium_capacity = int(input())
fans_count = int(input())

sectors = {
    'A': 0,
    'B': 0,
    'V': 0,
    'G': 0,
}

for _ in range(fans_count):
    sector = input()
    if sector in sectors:
        sectors[sector] += 1

percentage_A = (sectors['A'] / fans_count) * 100
percentage_B = (sectors['B'] / fans_count) * 100
percentage_V = (sectors['V'] / fans_count) * 100
percentage_G = (sectors['G'] / fans_count) * 100
percentage_all_fans = (fans_count / stadium_capacity) * 100

print(f'{percentage_A:.2f}%')
print(f'{percentage_B:.2f}%')
print(f'{percentage_V:.2f}%')
print(f'{percentage_G:.2f}%')
print(f'{percentage_all_fans:.2f}%')
