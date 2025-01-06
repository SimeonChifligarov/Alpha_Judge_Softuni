def calculate_euros():
    bitcoins = int(input())
    yuan = float(input())
    commission_percent = float(input())

    bitcoin_to_bgn = bitcoins * 1168
    yuan_to_bgn = yuan * 0.15 * 1.76
    total_bgn = bitcoin_to_bgn + yuan_to_bgn

    euros = total_bgn / 1.95
    commission = euros * (commission_percent / 100)

    result = euros - commission
    print(f'{result:.2f}')


if __name__ == '__main__':
    calculate_euros()
