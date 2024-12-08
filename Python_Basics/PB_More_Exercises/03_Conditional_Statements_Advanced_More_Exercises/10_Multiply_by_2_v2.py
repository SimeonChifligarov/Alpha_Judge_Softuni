MULTIPLIER = 2

prints = []

num = float(input())
while num >= 0:
    result = num * MULTIPLIER
    prints.append(f'Result: {result :.2f}')
    num = float(input())

prints.append('Negative number!')

print(*prints, sep='\n')
