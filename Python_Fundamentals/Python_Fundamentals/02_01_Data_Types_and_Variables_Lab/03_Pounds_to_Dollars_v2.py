def convert_pounds_to_dollars(pounds):
    return pounds * 1.31


if __name__ == '__main__':
    british_pounds = int(input())
    us_dollars = convert_pounds_to_dollars(pounds=british_pounds)
    print(f'{us_dollars:.3f}')
