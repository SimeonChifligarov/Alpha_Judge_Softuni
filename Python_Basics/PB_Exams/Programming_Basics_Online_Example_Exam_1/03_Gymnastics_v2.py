def calculate_score(country, apparatus):
    scores = {
        'Russia': {
            'ribbon': (9.100, 9.400),
            'hoop': (9.300, 9.800),
            'rope': (9.600, 9.000),
        },
        'Bulgaria': {
            'ribbon': (9.600, 9.400),
            'hoop': (9.550, 9.750),
            'rope': (9.500, 9.400),
        },
        'Italy': {
            'ribbon': (9.200, 9.500),
            'hoop': (9.450, 9.350),
            'rope': (9.700, 9.150),
        }
    }

    max_score = 20.0

    difficulty, execution = scores[country][apparatus]
    total_score = difficulty + execution

    missing_percentage = ((max_score - total_score) / max_score) * 100

    result = [
        f'The team of {country} get {total_score:.3f} on {apparatus}.',
        f'{missing_percentage:.2f}%',
    ]

    return result


c_country = input()
c_apparatus = input()

res = calculate_score(c_country, c_apparatus)
print('\n'.join(res))
