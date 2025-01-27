def convert_pounds_to_dollars(pounds, rate):
    return pounds * rate


if __name__ == '__main__':
    CONVERSION_RATE_POUND_TO_DOLLAR = 1.31
    british_pounds = int(input())
    us_dollars = convert_pounds_to_dollars(pounds=british_pounds, rate=CONVERSION_RATE_POUND_TO_DOLLAR)
    print(f'{us_dollars:.3f}')
