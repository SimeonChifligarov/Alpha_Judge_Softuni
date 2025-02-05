def check_brackets(n: int) -> str:
    last_bracket = ''
    for _ in range(n):
        line = input()
        if line == '(':
            if last_bracket == '(':
                return 'UNBALANCED'
            last_bracket = '('
        elif line == ')':
            if last_bracket != '(':
                return 'UNBALANCED'
            last_bracket = ''
    return 'BALANCED' if last_bracket == '' else 'UNBALANCED'


if __name__ == '__main__':
    n_input = int(input())
    result = check_brackets(n=n_input)
    print(result)
