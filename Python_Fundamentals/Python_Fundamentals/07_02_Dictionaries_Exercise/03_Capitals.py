countries = input().split(', ')
capitals = input().split(', ')

countries_zip = zip(countries, capitals)
# print(list(countries_zip))
# print(type(countries_zip))  # <class 'zip'>

# result = {el[0]: el[1] for el in countries_dict}
result = {country: capital for country, capital in countries_zip}

for cntr, cptl in result.items():
    print(f'{cntr} -> {cptl}')
