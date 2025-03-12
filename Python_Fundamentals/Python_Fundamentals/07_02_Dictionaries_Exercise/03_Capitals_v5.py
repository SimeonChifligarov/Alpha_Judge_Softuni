def map_countries_to_capitals(countries: list[str], capitals: list[str]) -> dict[str, str]:
    """
    Maps countries to their corresponding capitals using dictionary comprehension.
    """
    return {country: capital for country, capital in zip(countries, capitals)}


def print_country_capitals(country_capital_map: dict[str, str]) -> None:
    """
    Prints each country with its capital in the required format.
    """
    for country, capital in country_capital_map.items():
        print(f'{country} -> {capital}')


if __name__ == '__main__':
    countries_input = input().split(', ')
    capitals_input = input().split(', ')
    result = map_countries_to_capitals(countries=countries_input, capitals=capitals_input)
    print_country_capitals(country_capital_map=result)
