def classify_number(num):
    if num == 0:
        return 'zero'
    result = ''
    if abs(num) < 1:
        result += 'small '
    elif abs(num) > 1_000_000:
        result += 'large '
    result += 'positive' if num > 0 else 'negative'
    return result.strip()


if __name__ == '__main__':
    user_input = float(input())
    output = classify_number(num=user_input)
    print(output)
