countries = input().split(', ')
capitals = input().split(', ')

result = {}

for i in range(len(countries)):
    result[countries[i]] = capitals[i]

for country, capital in result.items():
    print(f'{country} -> {capital}')
