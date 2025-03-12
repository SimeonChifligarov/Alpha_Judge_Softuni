def map_countries_to_capitals():
    countries = input().split(', ')
    capitals = input().split(', ')

    country_capital_map = {country: capital for country, capital in zip(countries, capitals)}

    for country, capital in country_capital_map.items():
        print(f'{country} -> {capital}')


if __name__ == '__main__':
    map_countries_to_capitals()
