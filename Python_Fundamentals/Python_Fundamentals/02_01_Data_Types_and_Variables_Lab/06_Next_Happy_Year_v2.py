def find_next_happy_year(starting_year):
    next_year = starting_year + 1
    while len(set(str(next_year))) < len(str(next_year)):
        next_year += 1
    return next_year


if __name__ == '__main__':
    input_year = int(input())
    result = find_next_happy_year(starting_year=input_year)
    print(result)
